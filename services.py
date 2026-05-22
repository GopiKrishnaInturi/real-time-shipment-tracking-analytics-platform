from sqlalchemy.orm import Session
from models import Shipment, ShipmentEvent

def create_shipment(db: Session, payload):
    shipment = Shipment(**payload.dict())
    db.add(shipment)
    db.commit()
    db.refresh(shipment)
    return shipment

def create_event(db: Session, payload):
    event = ShipmentEvent(**payload.dict())
    db.add(event)
    db.commit()
    db.refresh(event)
    return event