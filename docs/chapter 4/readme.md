# 🏥 FastAPI DevOps Project

A production-style Patient Management REST API built with **FastAPI** while learning **DevOps, Cloud, Docker, Kubernetes, Terraform, CI/CD, Monitoring, and AWS** from scratch.

This repository is being developed chapter-by-chapter as part of a complete DevOps learning roadmap.

---

# 🚀 Tech Stack

- Python 3.13
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic v2
- Uvicorn
- Pytest
- python-dotenv

---

# 📂 Project Structure

```
fastapi-devops-project/
│
├── app/
│   ├── api/
│   │   └── routes/
│   ├── core/
│   ├── database/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── utils/
│
├── docs/
├── iam/
├── kubernetes/
├── monitoring/
├── scripts/
├── terraform/
├── tests/
│
├── main.py
├── requirements.txt
├── Dockerfile
├── .env
├── .gitignore
└── README.md
```

---

# 📚 Completed Chapters

## ✅ Chapter 1 – Project Initialization

- Created GitHub Repository
- Created Python Virtual Environment
- Installed FastAPI & Uvicorn
- Created first FastAPI application
- Verified API using Swagger UI
- Git setup and initial push

---

## ✅ Chapter 2 – FastAPI Fundamentals

Implemented REST APIs

- GET
- POST
- PUT
- DELETE

Added

- Path Parameters
- Query Parameters
- Request Validation
- Pydantic Models
- BMI Calculation
- Error Handling

---

## ✅ Chapter 3 – SQLite & SQLAlchemy

Migrated from JSON storage to SQLite Database.

Completed

- SQLAlchemy ORM
- Database Connection
- Database Models
- CRUD Operations
- Automatic Table Creation
- Database Sessions
- SQLite Integration

---

## ✅ Chapter 4 – Project Refactoring

Converted the project into a production-style folder structure.

Completed

### 📁 Project Structure

- Modular package architecture
- Routes separated
- Models separated
- Schemas separated
- Database module
- Core module
- Services folder
- Utils folder

### ⚙ Configuration

- Environment Variables
- `.env`
- `python-dotenv`
- Config module

### 🛡 Exception Handling

- Centralized exception handlers
- Custom HTTP error responses

### ❤️ Health Check

- `/health` endpoint

### 🧪 Testing

- Pytest installed
- First API test
- Health endpoint testing

### 📦 Dependencies

- requirements.txt generated

---

# 📌 Current API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Home |
| GET | /about | About API |
| GET | /view | View all patients |
| GET | /patient/{id} | View patient |
| GET | /sort | Sort patients |
| POST | /create | Create patient |
| PUT | /update/{id} | Update patient |
| DELETE | /delete/{id} | Delete patient |
| GET | /health | Health Check |

---

# ▶ Running the Project

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run FastAPI

```bash
uvicorn main:app --reload
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

Health Check

```
http://127.0.0.1:8000/health
```

---

# 🧪 Run Tests

```bash
python -m pytest
```

---

# 📖 Upcoming Chapters

- ⏳ Chapter 5 — Docker
- ⏳ Chapter 6 — Docker Compose
- ⏳ Chapter 7 — Jenkins CI/CD
- ⏳ Chapter 8 — Kubernetes
- ⏳ Chapter 9 — Monitoring (Grafana & Prometheus)
- ⏳ Chapter 10 — Terraform
- ⏳ Chapter 11 — AWS Deployment
- ⏳ Chapter 12 — Production CI/CD Pipeline

---

# 🎯 Learning Goals

This project demonstrates hands-on implementation of:

- REST API Development
- Database Design
- Project Architecture
- Environment Configuration
- Automated Testing
- Docker
- Kubernetes
- CI/CD
- Infrastructure as Code
- Cloud Deployment
- Monitoring
- DevOps Best Practices

---

# 👨‍💻 Author

**Naiyar Ansari**

DevOps & Cloud Engineer

GitHub: https://github.com/naiyar25