from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TruckDriver(Base):
    __tablename__ = "drivers"
    
    id = Column(Integer, primary_key=True, index=True)
    license_number = Column(String(20), unique=True)
    full_name = Column(String(100))
    date_of_birth = Column(Date)
    blood_type = Column(String(3))
    vehicle_type = Column(String(50))  # "Tractor-Trailer", "Straight Truck", etc.
    provinces = Column(String(100))  # "AB,BC,ON"
    has_hazmat = Column(Boolean)
    years_experience = Column(Integer)
    medical_expiry = Column(Date)
