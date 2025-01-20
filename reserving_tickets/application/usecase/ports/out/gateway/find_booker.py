from reserving_tickets.domain.exception.missing_booker_exception import MissingBookerException


class FindBooker:
    def findByUsername(self, bookerUsername):
        pass

    def findByUsernameOrThrow(self, bookerUsername):
        booker = self.findByUsername(bookerUsername)
        if booker is None:
            raise MissingBookerException("Booker not found")
        return booker