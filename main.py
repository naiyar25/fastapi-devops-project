from fastapi import FastAPI

from app.database.database import engine
from app.models import patient as patient_model
from app.api.routes.patient import router

patient_model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Patient Management API",
    version="1.0.0"
)

app.include_router(router)