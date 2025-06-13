from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import date
import models, schemas
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/drivers/", response_model=schemas.DriverCreate)
def create_driver(driver: schemas.DriverCreate, db: Session = Depends(get_db)):
    db_driver = models.TruckDriver(
        **driver.dict(),
        provinces=",".join(driver.provinces)  # Convert list to string
    db.add(db_driver)
    db.commit()
    db.refresh(db_driver)
    return db_driver

@app.get("/drivers/{license_number}")
def get_driver(license_number: str, db: Session = Depends(get_db)):
    driver = db.query(models.TruckDriver).filter(
        models.TruckDriver.license_number == license_number).first()
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver 
