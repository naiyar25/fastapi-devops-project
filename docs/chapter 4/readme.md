# Chapter 4 - FastAPI Project Structure & CRUD API

## 📖 Objective

The objective of this chapter was to build a production-ready FastAPI application with proper project structure, SQLite database integration, SQLAlchemy ORM, and complete CRUD operations.

---

# 🛠 Technologies Used

- Python 3.x
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- Pydantic
- Git
- GitHub

---

# 📂 Project Structure

```
fastapi-devops-project/
│
├── app/
│   ├── api/
│   │   └── routes/
│   │       └── patient.py
│   │
│   ├── database/
│   │   └── database.py
│   │
│   ├── models/
│   │   └── patient.py
│   │
│   ├── schemas/
│   │   └── patient.py
│   │
│   ├── services/
│   ├── utils/
│   └── core/
│
├── docs/
│   └── chapter4/
│       └── README.md
│
├── patients.db
├── requirements.txt
├── main.py
└── venv/
```

---

# 📁 Folder Description

| Folder | Description |
|---------|-------------|
| api/routes | Contains all API endpoints |
| database | Database connection and session |
| models | SQLAlchemy ORM models |
| schemas | Pydantic request/response models |
| services | Business logic (Future use) |
| utils | Helper functions (Future use) |
| core | Application configuration (Future use) |

---

# 🗄 Database

Database Used:

- SQLite

Database File:

```
patients.db
```

ORM:

- SQLAlchemy

---

# 📋 Patient Model

Fields stored in the database:

- ID
- Name
- City
- Age
- Gender
- Height
- Weight
- BMI
- Verdict

BMI and Verdict are automatically calculated using Pydantic computed fields.

---

# 🌐 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Welcome API |
| GET | /about | About API |
| GET | /view | View all patients |
| GET | /patient/{id} | View single patient |
| GET | /sort | Sort patients |
| POST | /create | Create patient |
| PUT | /update/{id} | Update patient |
| DELETE | /delete/{id} | Delete patient |

---

# ▶ Running the Project

## Activate Virtual Environment

Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start FastAPI Server

```bash
uvicorn main:app --reload
```

---

## Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# 🧪 Features Implemented

- Project restructuring
- SQLite integration
- SQLAlchemy ORM
- CRUD APIs
- Automatic BMI calculation
- Automatic health verdict calculation
- Swagger documentation
- Request validation using Pydantic
- Database dependency injection

---

# 🐞 Issues Resolved

During this chapter the following issues were resolved:

- Fixed Git repository structure
- Fixed nested project folder
- Fixed import path issues
- Refactored project into modules
- Fixed SQLAlchemy model imports
- Fixed Pydantic validation issues
- Fixed PatientDTO attribute error
- Organized routes using APIRouter

---

# 📚 Key Concepts Learned

- FastAPI project architecture
- APIRouter
- Dependency Injection
- SQLAlchemy ORM
- SQLite database
- Pydantic schemas
- CRUD operations
- Request validation
- JSON responses
- Project refactoring
- Modular application structure

---

# 🎯 Chapter Outcome

By completing this chapter, I successfully built a modular FastAPI application with a production-style folder structure, integrated SQLite using SQLAlchemy, implemented complete CRUD operations, and organized the API using APIRouter for better maintainability.

---

# ✅ Chapter Status

**Completed Successfully**