# CI/CD Pipeline Reference

## Full Pipeline Overview

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BACKEND (FastAPI)                    FRONTEND (React)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[DEVELOPMENT]
Developer writes code                Developer writes code
↓                                    ↓
git push → feature branch            git push → feature branch
↓                                    ↓
Pull Request                         Pull Request
↓                                    ↓
CI triggers:                         CI triggers:
├── pytest                           ├── npm run test
├── flake8 (lint)                    ├── npm run lint
└── docker build test                └── npm run build
↓                                    ↓
Code review                          Code review
↓                                    ↓
Merge to main                        Merge to main

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[STAGING]
CD triggers:                         CD triggers:
├── inject staging secrets           ├── inject staging secrets
│   ├── POSTGRES_USER                │   ├── REACT_APP_API_URL
│   ├── POSTGRES_PASSWORD            │   └── REACT_APP_USE_MOCK=false
│   └── POSTGRES_DB                  │
├── build Docker image               ├── npm run build
├── push to Docker Hub               └── deploy to Vercel (staging)
├── deploy to staging server              ↑
├── run alembic migrations           WAITS for backend staging
└── health check                     to pass health check
         ↓
    BACKEND READY
         ↓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
         QA / teammates test on staging
         Fix bugs → push → repeat staging
         ↓
    Approve for production
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[PRODUCTION]
CD triggers:                         CD triggers:
├── inject production secrets        ├── inject production secrets
│   ├── POSTGRES_USER                │   └── REACT_APP_API_URL
│   ├── POSTGRES_PASSWORD            │       =https://api.yoursite.com
│   └── POSTGRES_DB                  │
├── pull Docker image                ├── npm run build
├── deploy to production server      └── deploy to Vercel (production)
├── run alembic migrations                ↑
├── health check                     WAITS for backend production
└── rollback if fails                to pass health check
```

---

## ENV Vars Location

| Stage | Backend | Frontend |
|---|---|---|
| Development | `.env.development` on your machine | `.env.development` on your machine |
| Staging | GitHub Secrets (backend repo) | GitHub Secrets (frontend repo) |
| Production | GitHub Secrets (backend repo) | GitHub Secrets (frontend repo) |

### Backend secrets
```
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_DB
```

### Frontend secrets
```
REACT_APP_API_URL=https://api.yoursite.com      # production
REACT_APP_API_URL=https://staging-api.yoursite.com  # staging
REACT_APP_USE_MOCK=false
```

---

## Deployment Order (always)

```
1. Backend deploys first
2. Alembic migrations run
3. Health check passes
4. Frontend deploys
```

Never deploy frontend before backend — the new UI may call endpoints that don't exist yet.

---

## Tools

| Purpose | Tool |
|---|---|
| CI/CD pipeline | GitHub Actions |
| Docker image storage | Docker Hub / AWS ECR |
| Backend hosting | AWS / Railway / Render |
| Frontend hosting | Vercel / Netlify |
| Database migrations | Alembic |
| Backend tests | Pytest |
| Frontend tests | Jest / Vitest |
| Code linting | flake8 (Python), ESLint (JS) |

---

## Key Rules

- **Never commit `.env` files** — use GitHub Secrets for staging/production
- **Never skip staging** — always test there before production
- **Backend deploys first** — always, every time
- **Rollback automatically** if health check fails after deployment
- **Commit `.env.example`** with empty values so teammates know what vars are needed

---

## .gitignore for env files

```
.env
.env.development
.env.staging
.env.production
```

Only commit:
```
.env.example   ← safe, no real values
```

---

## What Software Engineers Need to Know

| Level | Expectation |
|---|---|
| Junior | Understand the flow, can read a pipeline |
| Mid | Can write and debug GitHub Actions |
| Senior | Can design the full pipeline, optimize it |
| DevOps | Deep expertise — Kubernetes, Terraform, monitoring |
