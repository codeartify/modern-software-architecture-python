class BookerId:
    def __init__(self, value):
        if value is None or value < 0:
            raise ValueError("BookerId must be greater than 0")
        self._value = value

    def value(self):
        return self._value
