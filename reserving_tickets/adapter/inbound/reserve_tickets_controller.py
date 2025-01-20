from fastapi import APIRouter, HTTPException, Path, Body
import logging

from reserving_tickets.application.usecase.reserve_tickets_use_case import ReserveTicketsUseCase

log = logging.getLogger(__name__)

router = APIRouter(prefix="/api")

# Constructing usecase with gateways (we assume implementations given below)
reserveTickets = ReserveTicketsUseCase(FindBookerImpl(), FindEventImpl(), UpdateEventImpl())

@router.post("/events/{id}/tickets")
def reserveTicketsForEvent(
    id: int = Path(...),
    reserveTicketsRequest: ReserveTicketsRequest = Body(...)
):
    log.info("Reserving tickets for event with ID: %s", id)
    log.info("Reserve tickets request: %s", reserveTicketsRequest)

    ticketType = reserveTicketsRequest.ticketType
    numberOfTickets = reserveTicketsRequest.numberOfTickets
    bookerUsername = reserveTicketsRequest.bookerUsername

    log.info("Reserving %d tickets of type %s for user %s", numberOfTickets, ticketType, bookerUsername)

    presenter = ReserveTicketsForEventPresenter()
    reserveTicketsInput = reserveTicketsInput = reserveTickets.withValid(id, ticketType, numberOfTickets, bookerUsername) # We'll need to fix this line, see below

    # Actually, ReserveTicketsInput is created from a static method in the original code:
    from reserving_tickets.application.usecase.reserve_tickets_input import ReserveTicketsInput
    reserveTicketsInput = ReserveTicketsInput.withValid(id, ticketType, numberOfTickets, bookerUsername)

    # execute
    reserveTickets.execute(reserveTicketsInput, presenter, presenter)

    if presenter.hasError():
        err = presenter.getError()
        log.error("Error reserving tickets: %s", err)
        # Construct response as per error
        if err["status_code"] == 404:
            raise HTTPException(status_code=404)
        elif err["status_code"] == 204:
            # 204 No Content
            return "", 204
        elif err["status_code"] == 400:
            raise HTTPException(status_code=400, detail=err["body"])
        else:
            raise HTTPException(status_code=500, detail=err["body"])
    else:
        success = presenter.getSuccess()
        log.info("Successfully reserved tickets: %s", success)
        return success["body"]  # 200 OK by default
