from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from schemas import ShipmentCreate, EventCreate
from services import create_shipment, create_event

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/shipments")
def add_shipment(payload: ShipmentCreate, db: Session = Depends(get_db)):
    return create_shipment(db, payload)

@router.post("/events")
def add_event(payload: EventCreate, db: Session = Depends(get_db)):
    return create_event(db, payload)

@router.get("/health")
def health():
    return {"status": "running"}