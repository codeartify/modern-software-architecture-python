# domain/selected_event.py
from reserving_tickets.domain.exception.number_of_tickets_per_buyer_exceeded_exception import \
    NumberOfTicketsPerBuyerExceededException


class SelectedEvent:
    def __init__(self, event_id, tickets_left, number_of_tickets_per_booker):
        self.id = event_id
        self._tickets_left = tickets_left
        self._number_of_tickets_per_booker = number_of_tickets_per_booker

    def get_id(self):
        return self.id

    def tickets_left(self):
        return self._tickets_left

    def exceeds_number_of_tickets_per_booker(self, requested_number_of_tickets):
        return self._number_of_tickets_per_booker.value() < requested_number_of_tickets.value()

    def book_tickets(self, booker, requested_number_of_tickets, ticket_type):
        if self.exceeds_number_of_tickets_per_booker(requested_number_of_tickets):
            raise NumberOfTicketsPerBuyerExceededException("Cannot reserve more tickets than allowed per buyer")

        self._tickets_left.markTicketsAsReserved(booker, ticket_type, requested_number_of_tickets)

