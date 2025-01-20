class Booker:
    def __init__(self, bookerId, username):
        self._id = bookerId
        self._username = username

    def id(self):
        return self._id

    def username(self):
        return self._username
