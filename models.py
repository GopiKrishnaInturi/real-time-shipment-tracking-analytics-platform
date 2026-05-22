from sqlalchemy import Column, Integer, String, DateTime
from database import Base
import datetime

class Shipment(Base):
    __tablename__ = "shipments"

    id = Column(Integer, primary_key=True, index=True)
    tracking_number = Column(String, unique=True)
    status = Column(String)
    source = Column(String)
    destination = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class ShipmentEvent(Base):
    __tablename__ = "shipment_events"

    id = Column(Integer, primary_key=True, index=True)
    tracking_number = Column(String)
    event_type = Column(String)
    location = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)