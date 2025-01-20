from .database import Base
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship

# This is a simplification. The actual schema and queries might differ.
# In the original code, "event", "ticket", "booker" tables exist.
# We'll define them similarly.

class BookerEntity(Base):
    __tablename__ = "booker"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=False)

class EventEntity(Base):
    __tablename__ = "event"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tickets_per_booker = Column(Integer, nullable=False)

    # relationship to tickets is defined inbound TicketEntity
    tickets = relationship("TicketEntity", back_populates="event")

class TicketEntity(Base):
    __tablename__ = "ticket"
    id = Column(Integer, primary_key=True, autoincrement=True)
    event_id = Column(Integer, ForeignKey("event.id"))
    type = Column(String(50), nullable=False)
    booker_id = Column(Integer, ForeignKey("booker.id"), nullable=True)

    event = relationship("EventEntity", back_populates="tickets")
