class AllTicketsSoldException(IllegalArgumentException := type('IllegalArgumentException', (Exception,), {})):
    def __init__(self, message):
        super().__init__(message)
