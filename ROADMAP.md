# Mid-Level Engineer Roadmap

## Current Status
- 2-3 deployed projects
- Client work experience
- Learning FastAPI + Docker + CI/CD

---

## Phase 1 — Solidify Backend (1-2 months)

### FastAPI
- [ ] Path & query parameters
- [ ] Request body with Pydantic models
- [ ] HTTP methods (GET, POST, PUT, DELETE)
- [ ] Status codes & error handling (HTTPException)
- [ ] Dependency injection (Depends)
- [ ] Routers (split app into multiple files)
- [ ] Middleware (CORS)
- [ ] Async/await endpoints

### Database
- [ ] SQLAlchemy — define models, query data
- [ ] Alembic — create and run migrations
- [ ] Relationships (one-to-many, many-to-many)
- [ ] Basic query optimization

### Authentication
- [ ] JWT — login, token generation, token validation
- [ ] Protected routes with Depends
- [ ] Password hashing (bcrypt)
- [ ] Refresh tokens

---

## Phase 2 — Testing (2-3 weeks)

### Backend
- [ ] Pytest basics
- [ ] Testing FastAPI endpoints (TestClient)
- [ ] Testing with a real test database
- [ ] Write tests for auth endpoints
- [ ] Write tests for CRUD endpoints

### Frontend (when relevant)
- [ ] Jest basics
- [ ] Testing React components
- [ ] Testing API calls (mock fetch)

---

## Phase 3 — DevOps (1-2 months)

### Docker
- [ ] Write a Dockerfile for FastAPI
- [ ] Write a Dockerfile for React
- [ ] docker-compose for local dev (DB + backend + frontend)
- [ ] Multi-stage builds (smaller production image)

### CI/CD
- [ ] Write a GitHub Actions pipeline for backend
- [ ] Write a GitHub Actions pipeline for frontend
- [ ] Auto-run tests on pull request
- [ ] Auto-deploy to staging on merge to main
- [ ] Manual deploy to production

### Cloud
- [ ] Deploy backend to Railway or Render
- [ ] Deploy frontend to Vercel
- [ ] Set up environment variables in cloud provider
- [ ] Set up a real staging environment

---

## Phase 4 — Level Up (ongoing)

### API Design
- [ ] Proper error responses (consistent format)
- [ ] Pagination
- [ ] Filtering & sorting
- [ ] API versioning (/v1/products)

### Security
- [ ] Input validation
- [ ] Rate limiting
- [ ] HTTPS only in production
- [ ] SQL injection awareness
- [ ] Never expose stack traces in production

### Git & Collaboration
- [ ] Feature branch workflow
- [ ] Writing good PRs
- [ ] Writing good commit messages
- [ ] Code review etiquette

### System Design Basics
- [ ] How to think about scaling
- [ ] Load balancers
- [ ] Caching basics (Redis)
- [ ] Background jobs (when not to do everything in a request)

---

## Project Checklist
For each project, make sure it has:
- [ ] Deployed to a real URL (not localhost)
- [ ] JWT authentication
- [ ] PostgreSQL with migrations
- [ ] Docker + docker-compose
- [ ] GitHub Actions CI/CD pipeline
- [ ] Staging + production environments
- [ ] Basic tests
- [ ] .env.example committed, .env never committed
- [ ] README explaining what it does and how to run it

---

## Milestone Targets

```
Now          →  Junior (44k THB) — deployed projects, basic skills
+3 months    →  Stronger junior — auth, testing, Docker done
+6 months    →  Mid-level ready — full CI/CD, cloud, system design basics
+1 year      →  Mid-level (50k-100k THB) — real projects with all layers
```

---

## Key Reminder
One real shipped project with all layers beats five tutorial clones.
Depth over breadth.
