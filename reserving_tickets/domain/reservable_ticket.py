from reserving_tickets.domain.booker_id import BookerId
from reserving_tickets.domain.ticket_type import TicketType


class ReservableTicket:
    def __init__(self, booker_id: BookerId, ticket_type: TicketType):
        self._booker_id = booker_id
        self._ticket_type = ticket_type

    def booked_by(self, booker_id):
        self._booker_id = booker_id

    def booker_id(self):
        return self._booker_id

    def ticket_type(self):
        return self._ticket_type

    def can_be_reserved(self):
        return not self.is_reserved()

    def is_reserved(self):
        return self._booker_id is not None

    def is_of_type(self, ticket_type):
        return self._ticket_type == ticket_type

    def is_requested_ticket(self, ticket_type):
        return self.is_of_type(ticket_type) and self.can_be_reserved()
