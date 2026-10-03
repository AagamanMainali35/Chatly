# FastAPI Project Management & RBAC Backend

A high-performance, asynchronous backend built with FastAPI, SQLAlchemy 2.0 (asyncio), PostgreSQL, Alembic migrations, Redis, and Celery.

---

## Features

- **Asynchronous Architecture**: Full async database operations with SQLAlchemy 2.0 and `asyncpg`.
- **Authentication & Security**:
  - Secure password hashing via `pwdlib`.
  - JWT Bearer Token validation and token generation (`access` & `refresh`).
  - Custom `AuthMiddleware` protecting endpoints with public route whitelisting.
- **Role-Based Access Control (RBAC)**:
  - Dynamic Roles & Permissions schema with `role_permissions` composite key mapping.
  - Protection for system roles (`is_system` flag).
- **Database Migrations**: Managed via Alembic with automated revision and async upgrade/downgrade workflows.
- **Interactive Seeding**: CLI utilities (`scripts/seed_role.py`, `scripts/seed_user.py`) with `rich` library formatting.
- **Containerization**: Multi-stage Docker build with non-root security context and Docker Compose integration (PostgreSQL + Redis + Celery + FastAPI).

---

## Tech Stack

| Technology | Purpose |
|---|---|
| **FastAPI** | High-performance asynchronous API framework |
| **SQLAlchemy (Async)** | Async ORM & query builder |
| **PostgreSQL** | Primary relational database |
| **Alembic** | Database schema migrations |
| **Redis** | In-memory cache & message broker |
| **Celery** | Asynchronous background worker |
| **uv** | Ultra-fast Python package & project manager |
| **Docker & Compose** | Containerized development & production runtime |

---

## Project Structure

```
├── alembic/                # Database migrations and configuration
│   └── versions/           # Versioned migration scripts
├── app/
│   ├── config/             # Settings (Pydantic BaseSettings) & async database session
│   ├── controller/         # API Routers (auth, roles, permissions)
│   ├── models/             # SQLAlchemy ORM models & Pydantic schemas
│   ├── repository/         # Data access & database queries
│   ├── services/           # Business logic layer
│   └── utils/              # Password hashing, JWT token handling & auth helpers
├── scripts/                # Database seeding CLI scripts
├── dockerfile              # Optimized multi-stage Docker build
├── docker-compose.yml      # Multi-container orchestration (DB, Redis, App, Celery)
├── makefile                # Handy dev commands (run, mm, mig, rollback)
├── pyproject.toml          # Project dependencies & packaging
└── README.md
```

---

## Quickstart

### 1. Environment Setup
Copy the sample environment file:
```bash
cp .env.sample .env
```
Ensure `DATABASE_URL`, `SECRET_KEY`, and `CORS_ALLOWED_ORIGINS` are properly set.

### 2. Run Database Migrations
```bash
make mig
```

### 3. Run the Development Server
```bash
make run
```
The server will start at `http://localhost:8000` with Swagger docs available at `http://localhost:8000/docs`.

### 4. Seed Roles & Users
```bash
uv run python scripts/seed_role.py
uv run python scripts/seed_user.py
```

---

## API Overview

### Health
- `GET /health`: Health check endpoint.

### Authentication (`/`)
- `POST /register`: Register a new user with default role.
- `POST /login`: Authenticate and obtain JWT tokens.
- `POST /change-password`: Update existing user password.
- `POST /reset-password`: Initiate password reset flow.

### Roles (`/roles`)
- `GET /roles/all`: List all roles with associated permissions.
- `GET /roles/{role_id}`: Retrieve role details by ID.
- `POST /roles/create`: Create a new role with assigned permissions.
- `PUT /roles/update/{role_id}`: Update role name and permission mappings.
- `DELETE /roles/delete/{role_id}`: Remove role.

### Permissions (`/permissions`)
- `GET /permissions/all`: List all available permissions.
- `POST /permissions/ids`: Bulk retrieve permissions by ID list.
- `GET /permissions/name/{name}`: Get permission by unique name.
- `POST /permissions/create`: Create new permission.
- `GET /permissions/{id}`: Get permission by ID.
- `PATCH /permissions/update/{id}`: Partially update permission details.
- `DELETE /permissions/delete/{id}`: Delete permission.

---

## License
MIT
