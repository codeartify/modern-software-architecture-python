from enum import Enum


class TicketType(Enum):
    STANDARD = "STANDARD"
    VIP = "VIP"

    @staticmethod
    def get_value_of(type_str):
        return TicketType[type_str.upper()]
