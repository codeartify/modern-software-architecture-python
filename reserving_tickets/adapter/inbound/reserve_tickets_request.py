from pydantic import BaseModel, Field, constr

class ReserveTicketsRequest(BaseModel):
    numberOfTickets: int = Field(..., gt=0)
    ticketType: constr(regex='^(Standard|VIP)$')
    bookerUsername: str
