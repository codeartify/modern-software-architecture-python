class EventId:
    def __init__(self, value):
        if value is None:
            raise ValueError("EventId cannot be null")
        self._value = value

    def value(self):
        return self._value
