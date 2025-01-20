class ReserveTicketsOutput:
    def __init__(self, eventId, numberOfTickets, bookerUsername):
        self._eventId = eventId
        self._numberOfTickets = numberOfTickets
        self._bookerUsername = bookerUsername

    def eventId(self):
        return self._eventId

    def numberOfTickets(self):
        return self._numberOfTickets

    def bookerUsername(self):
        return self._bookerUsername
