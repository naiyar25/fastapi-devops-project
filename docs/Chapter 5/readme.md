# 🏥 FastAPI DevOps Project

A production-style Patient Management System built using **FastAPI** while learning **DevOps, Docker, AWS, Terraform, Kubernetes, Jenkins, Monitoring, and CI/CD** from scratch.

This repository is part of my complete DevOps learning journey where each chapter adds new production-ready features.

---

# 🚀 Tech Stack

- Python 3.13
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Docker
- Docker Compose
- Pytest
- Uvicorn
- Git & GitHub

---

# 📁 Project Structure

```
fastapi-devops-project/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── utils/
│
├── tests/
├── terraform/
├── monitoring/
├── kubernetes/
├── iam/
├── docs/
├── scripts/
│
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .env
├── requirements.txt
├── main.py
└── README.md
```

---

# ✅ Features Implemented

- Patient CRUD API
- SQLite Database Integration
- SQLAlchemy ORM
- Request Validation using Pydantic
- BMI Calculation
- Health Check Endpoint
- Centralized Exception Handling
- Environment Variable Configuration (.env)
- Unit Testing using Pytest
- Dockerized Application
- Docker Volumes
- Bind Mounts
- Docker Compose
- Docker Best Practices

---

# 🚀 Running Locally

## Clone Repository

```bash
git clone <repository-url>
cd fastapi-devops-project
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run FastAPI

```bash
uvicorn main:app --reload
```

Application

```
http://127.0.0.1:8000
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# 🐳 Docker

## Build Image

```bash
docker build -t patient-api:v1 .
```

---

## Run Container

```bash
docker run -d -p 8000:8000 --name patient-api-container patient-api:v1
```

---

# 💾 Docker Volume

Create Volume

```bash
docker volume create patient-data
```

Run with Volume

```bash
docker run -d -p 8000:8000 -v patient-data:/app --name patient-api-container patient-api:v1
```

---

# 📦 Docker Compose

Build

```bash
docker compose build
```

Run

```bash
docker compose up -d
```

Stop

```bash
docker compose down
```

View Logs

```bash
docker compose logs
```

---

# 🧪 Testing

Run all tests

```bash
python -m pytest -v
```

---

# 📚 Learning Progress

## ✅ Chapter 1

- Project Setup
- Git & GitHub

---

## ✅ Chapter 2

- FastAPI Fundamentals
- CRUD APIs
- Validation

---

## ✅ Chapter 3

- SQLite
- SQLAlchemy ORM
- Database Integration

---

## ✅ Chapter 4

- Project Restructuring
- Modular Architecture
- Configuration (.env)
- Health Check Endpoint
- Centralized Exception Handling
- Unit Testing (Pytest)

---

## ✅ Chapter 5

- Docker Fundamentals
- Dockerfile
- Images
- Containers
- Docker Commands
- Docker Volumes
- Bind Mounts
- Docker Compose
- Docker Best Practices
- Docker Interview Preparation

---

# 📌 Upcoming Chapters

- AWS
- Terraform
- Jenkins
- Kubernetes
- Monitoring
- CI/CD Pipeline
- Deployment
- Production Architecture

---

# 📖 API Documentation

Swagger

```
http://localhost:8000/docs
```

OpenAPI

```
http://localhost:8000/openapi.json
```

---

# 🎯 Project Goal

The objective of this project is to build a production-style FastAPI application while implementing real-world DevOps practices including containerization, infrastructure as code, CI/CD pipelines, monitoring, cloud deployment, and Kubernetes orchestration.

---

# 👨‍💻 Author

**Naiyar Ansari**

DevOps & Cloud Engineer

Learning in Public 🚀