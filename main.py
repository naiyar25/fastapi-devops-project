from fastapi import FastAPI

from app.database.database import engine
from app.models import patient as patient_model
from app.api.routes.patient import router
from app.api.routes.health import router as health_router
from app.core.exceptions import add_exception_handlers

patient_model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Patient Management API",
    version="1.0.0"
)

add_exception_handlers(app)

app.include_router(router)
app.include_router(health_router)