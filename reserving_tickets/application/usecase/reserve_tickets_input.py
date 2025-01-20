# application/usecase/reserve_tickets_input_output.py
class ReserveTicketsInput:
    def __init__(self, bookerUsername, eventId, numberOfTickets, ticketType):
        self._bookerUsername = bookerUsername
        self._eventId = eventId
        self._numberOfTickets = numberOfTickets
        self._ticketType = ticketType

    @staticmethod
    def withValid(eventId, ticketType, numberOfTickets, bookerUsername):
        return ReserveTicketsInput(
            BookerUsername(bookerUsername),
            EventId(eventId),
            NumberOfTickets(numberOfTickets),
            TicketType.getValueOf(ticketType)
        )

    def bookerUsername(self):
        return self._bookerUsername

    def eventId(self):
        return self._eventId

    def numberOfTickets(self):
        return self._numberOfTickets

    def ticketType(self):
        return self._ticketType

