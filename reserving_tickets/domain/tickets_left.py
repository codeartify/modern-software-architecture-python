from reserving_tickets.domain.exception.all_tickets_sold_exception import AllTicketsSoldException
from reserving_tickets.domain.exception.too_few_tickets_of_type_left_exception import TooFewTicketsOfTypeLeftException
from reserving_tickets.domain.reservable_ticket import ReservableTicket


class TicketsLeft:
    def __init__(self, tickets_left: [ReservableTicket]):
        self._tickets_left = tickets_left

    def tickets_left(self):
        return self._tickets_left

    def mark_tickets_as_reserved(self, booker, ticket_type, number_of_requested_tickets):
        if self.no_tickets_left():
            raise AllTicketsSoldException("No tickets left for the event")

        if self.not_enough_tickets_of_type_left(number_of_requested_tickets, ticket_type):
            raise TooFewTicketsOfTypeLeftException(
                "Not enough tickets of type " + ticket_type.name + " left for the event")

        for ticket in self._tickets_left:
            if ticket.isOfType(ticket_type):
                ticket.bookedBy(booker.id())
                number_of_requested_tickets.decrement()
                if number_of_requested_tickets.isZero():
                    break

    def not_enough_tickets_of_type_left(self, requested_number_of_tickets, ticket_type):
        return requested_number_of_tickets.value() > self.number_of_tickets_left_for_type(ticket_type)

    def number_of_tickets_left_for_type(self, ticket_type):
        return sum(1 for t in self._tickets_left if t.isRequestedTicket(ticket_type))

    def no_tickets_left(self):
        return not self.has_reservable_tickets()

    def has_reservable_tickets(self):
        return any(t.can_be_reserved() for t in self._tickets_left)
