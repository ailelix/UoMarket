import enum

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, BigInteger
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.sql import func


# Data Type
class ListingCondition(enum.Enum):
    NEW = "new"
    LIKE_NEW = "like_new"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"

class ListingStatus(enum.Enum):
    ACTIVE = "active"
    RESERVED = "reserved"
    SOLD = "sold"
    REMOVED = "removed"

class OrderEventType(enum.Enum):
    CREATED = "created"
    PAID = "paid"
    CANCELED = "canceled"
    COMPLETED = "completed"
    REFUNDED = "refunded"
    MESSAGE = "message"

class OrderStatus(enum.Enum):
    PLACED = "placed"
    PAID = "paid"
    CANCELED = "canceled"
    REFUNDED = "refunded"
    COMPLETED = "completed"


# Database Schema
class Listings(DeclarativeBase):
    __tablename__ = "listings"

    listing_id = Column(BigInteger, primary_key=True, autoincrement=True)
    seller_id = Column(BigInteger, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String)
    price_cents = Column(Integer, nullable=False)
    category_id = Column(BigInteger)
    status = Column(String, nullable=False)



