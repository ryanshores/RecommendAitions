# Setup

Vite + React-TS pairs best with a FastAPI backend for APIs, plus a dedicated auth setup (JWT or OAuth)

## FastAPI + React (Vite + TS)

* Type symmetry: FastAPI (Pydantic) + React-TS = clean contracts between FE/BE
* API-first (perfect for SPAs)
* Fast and async (auth, DB, third-party calls won’t block)
* OpenAPI → client generation (huge win for DX)

This is the setup most modern startups and internal platforms end up with.

## Auth & user profiles (the important part)

Recommended auth model

JWT + refresh tokens, stored securely

Typical flow:
1.	User logs in → backend issues:
*	access token (short-lived)
*	refresh token (long-lived, httpOnly cookie)
2.	React app stores access token in memory
3.	Refresh handled automatically

FastAPI libraries that actually work:
* fastapi-users (best all-in-one solution)
* Authlib (if you want OAuth / social login)
* python-jose or PyJWT (manual but flexible)

User profile handling
* users table (email, password hash, roles)
* profiles table (name, avatar, preferences, etc.)
* Profile API endpoints:

```
GET /me
PATCH /me
```

## Suggested FastAPI stack

Backend
*	FastAPI
*	SQLAlchemy 2.0 or SQLModel
*	Alembic (migrations)
*	PostgreSQL
*	fastapi-users (auth + user management)

Frontend
*	Vite
*	React
*	TypeScript
*	TanStack Query (React Query)
*	Axios or fetch wrapper
*	Zod (optional schema validation)

## Folder-level architecture (clean + scalable)

```
backend/
  app/
    main.py
    api/
      auth.py
      users.py
      profiles.py
    models/
    schemas/
    services/
    db/
frontend/
  src/
    api/
    auth/
    hooks/
    pages/
```