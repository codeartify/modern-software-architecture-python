class NumberOfTickets:
    def __init__(self, value):
        if value <= 0:
            raise ValueError("Number of tickets must be greater than 0")
        self._value = value

    def decrement(self):
        self._value -= 1

    def is_zero(self):
        return self._value == 0

    def value(self):
        return self._value
