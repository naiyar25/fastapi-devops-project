from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Path,
    Query,
)
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models import patient as patient_model
from app.schemas.patient import PatientDTO, PatientUpdate

router = APIRouter(
    prefix="",
    tags=["Patients"],
)


# -----------------------------
# Database Dependency
# -----------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -----------------------------
# Routes
# -----------------------------

@router.get("/")
def hello():
    return {"message": "Patient Management System API (SQL Version)"}


@router.get("/about")
def about():
    return {
        "message": "A fully functional API to manage your patients using SQLite."
    }


@router.get("/view")
def view(db: Session = Depends(get_db)):
    patients = db.query(patient_model.Patient).all()
    return patients


@router.get("/patient/{patient_id}")
def view_patient(
    patient_id: Annotated[
        str,
        Path(
            description="The ID of the patient in the database",
            example="P001",
        ),
    ],
    db: Session = Depends(get_db),
):
    db_patient = (
        db.query(patient_model.Patient)
        .filter(patient_model.Patient.id == patient_id)
        .first()
    )

    if not db_patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found",
        )

    return db_patient


@router.get("/sort")
def sort_patients(
    sort_by: str = Query(
        ...,
        description="Sort by height, weight or bmi",
    ),
    order: str = Query(
        "asc",
        description="asc or desc",
    ),
    db: Session = Depends(get_db),
):
    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sort field. Must be one of {valid_fields}",
        )

    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid order. Must be 'asc' or 'desc'",
        )

    patients = db.query(patient_model.Patient).all()

    sorted_data = sorted(
        patients,
        key=lambda x: getattr(x, sort_by),
        reverse=(order == "desc"),
    )

    return sorted_data


@router.post("/create")
def create_patient(
    patient_data: PatientDTO,
    db: Session = Depends(get_db),
):
    existing_patient = (
        db.query(patient_model.Patient)
        .filter(patient_model.Patient.id == patient_data.id)
        .first()
    )

    if existing_patient:
        raise HTTPException(
            status_code=400,
            detail="Patient with this ID already exists",
        )

    patient_dict = patient_data.model_dump()

    db_patient = patient_model.Patient(**patient_dict)

    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)

    return JSONResponse(
        content={"message": "Patient created successfully"},
        status_code=201,
    )


@router.put("/update/{patient_id}")
def update_patient(
    patient_id: str,
    patient_update: PatientUpdate,
    db: Session = Depends(get_db),
):
    db_patient = (
        db.query(patient_model.Patient)
        .filter(patient_model.Patient.id == patient_id)
        .first()
    )

    if not db_patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found",
        )

    update_data = patient_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_patient, key, value)

    current_data = {
        "id": db_patient.id,
        "name": db_patient.name,
        "city": db_patient.city,
        "age": db_patient.age,
        "gender": db_patient.gender,
        "height": db_patient.height,
        "weight": db_patient.weight,
    }

    temp_patient = PatientDTO(**current_data)

    db_patient.bmi = temp_patient.bmi
    db_patient.verdict = temp_patient.verdict

    db.commit()
    db.refresh(db_patient)

    return JSONResponse(
        content={"message": "Patient updated successfully"},
        status_code=200,
    )


@router.delete("/delete/{patient_id}")
def delete_patient(
    patient_id: str,
    db: Session = Depends(get_db),
):
    db_patient = (
        db.query(patient_model.Patient)
        .filter(patient_model.Patient.id == patient_id)
        .first()
    )

    if not db_patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found",
        )

    db.delete(db_patient)
    db.commit()

    return JSONResponse(
        content={"message": "Patient deleted successfully"},
        status_code=200,
    )