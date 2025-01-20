from reserving_tickets.application.usecase.ports.inbound.reserve_tickets import ReserveTickets
from reserving_tickets.application.usecase.ports.out.gateway.find_booker import FindBooker
from reserving_tickets.application.usecase.ports.out.gateway.find_event import FindEvent
from reserving_tickets.application.usecase.ports.out.gateway.update_event import UpdateEvent
from reserving_tickets.application.usecase.reserve_tickets_output import ReserveTicketsOutput


class ReserveTicketsUseCase(ReserveTickets):
    def __init__(self, findBooker: FindBooker, findEvent: FindEvent, updateEvent: UpdateEvent):
        self.findBooker = findBooker
        self.findEvent = findEvent
        self.updateEvent = updateEvent

    def execute(self, reserveTicketsInput, presentSuccess, presentFailure):
        try:
            booker = self.findBooker.findByUsernameOrThrow(reserveTicketsInput.bookerUsername())
            event = self.findEvent.findByIdOrThrow(reserveTicketsInput.eventId())

            event.bookTickets(booker, reserveTicketsInput.numberOfTickets(), reserveTicketsInput.ticketType())

            self.updateEvent.withValue(event)

            reserve_tickets_output = self.toOutput(reserveTicketsInput, event, booker)
            presentSuccess.present(reserve_tickets_output)
        except Exception as e:
            presentFailure.present(e)

    def toOutput(self, reserveTicketsInput, event, booker):
        return ReserveTicketsOutput(
            event.getId(),
            reserveTicketsInput.numberOfTickets(),
            booker.username()
        )