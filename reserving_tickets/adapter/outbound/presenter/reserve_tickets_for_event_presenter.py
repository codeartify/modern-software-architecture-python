
import logging

from reserving_tickets.application.usecase.ports.out.presenter.present_book_tickets_failure import \
    PresentBookTicketsFailure
from reserving_tickets.application.usecase.ports.out.presenter.present_book_tickets_success import \
    PresentBookTicketsSuccess

log = logging.getLogger(__name__)

class ReserveTicketsForEventPresenter(PresentBookTicketsSuccess, PresentBookTicketsFailure):
    def __init__(self):
        self.body = None
        self.error = None

    def present(self, arg):
        # Overloaded method in Java: one for success(ReserveTicketsOutput) and one for error(Exception).
        # In Python we must differentiate by checking the type.
        from reserving_tickets.application.usecase.reserve_tickets_output import ReserveTicketsOutput
        if isinstance(arg, ReserveTicketsOutput):
            # Success
            reserveTicketsOutput = arg
            self.body = ReserveTicketsResponse(
                reserveTicketsOutput.eventId().value(),
                reserveTicketsOutput.numberOfTickets().value(),
                reserveTicketsOutput.bookerUsername().value()
            )
        else:
            # Failure
            e = arg
            self.error = e

    # PresentBookTicketsSuccess
    def present(self, reserveTicketsOutput):
        self.body = ReserveTicketsResponse(
            reserveTicketsOutput.eventId().value(),
            reserveTicketsOutput.numberOfTickets().value(),
            reserveTicketsOutput.bookerUsername().value()
        )

    # PresentBookTicketsFailure
    def present_error(self, e: Exception):
        self.error = e

    def getError(self):
        if self.error is None:
            return None

        err_name = type(self.error).__name__
        if err_name in ["MissingBookerException", "MissingEventException"]:
            error_response = {"status_code": 404, "body": None}
        elif err_name in ["AllTicketsSoldException", "TooFewTicketsOfTypeLeftException"]:
            error_response = {"status_code": 204, "body": None}
        elif err_name == "NumberOfTicketsPerBuyerExceededException":
            error_response = {"status_code": 400, "body": self.error.args[0]}
        else:
            error_response = {"status_code": 500, "body": self.error.args[0]}

        log.error("Error: %s", self.error)
        return error_response

    def getSuccess(self):
        return {"status_code": 200, "body": self.body}

    def hasError(self):
        return self.error is not None
