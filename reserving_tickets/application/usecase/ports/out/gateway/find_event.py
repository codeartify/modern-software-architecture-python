from reserving_tickets.domain.exception.missing_event_exception import MissingEventException


class FindEvent:
    def findById(self, eventId):
        pass

    def findByIdOrThrow(self, eventId):
        event = self.findById(eventId)
        if event is None:
            raise MissingEventException("Event not found")
        return event
