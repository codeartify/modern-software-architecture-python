class ReserveTicketsResponse:
    def __init__(self, eventId, numberOfReservedTickets, bookerUsername):
        self.eventId = eventId
        self.numberOfReservedTickets = numberOfReservedTickets
        self.bookerUsername = bookerUsername
