class BookerUsername:
    def __init__(self, value):
        if not value:
            raise ValueError("Username cannot be blank")
        self._value = value

    def value(self):
        return self._value
