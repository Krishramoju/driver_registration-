from pydantic import BaseModel, Field, validator
from datetime import date
from typing import List

class DriverCreate(BaseModel):
    license_number: str = Field(..., min_length=5, max_length=20)
    full_name: str = Field(..., max_length=100)
    date_of_birth: date
    blood_type: str = Field(..., regex='^(A|B|AB|O)[+-]$')
    vehicle_type: str = Field(..., example="Tractor-Trailer")
    provinces: List[str] = Field(..., min_items=1)
    has_hazmat: bool
    years_experience: int = Field(..., ge=0)
    medical_expiry: date

    @validator('date_of_birth')
    def validate_age(cls, v):
        if (date.today() - v).days < 365*18:
            raise ValueError("Driver must be at least 18 years old")
        return v
