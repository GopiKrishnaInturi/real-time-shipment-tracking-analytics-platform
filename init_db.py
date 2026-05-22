from database import Base, engine
from models import Shipment, ShipmentEvent

Base.metadata.create_all(bind=engine)

print("Database initialized")