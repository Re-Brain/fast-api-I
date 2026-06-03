# Retired Racehorse Visit Scheduler

A web application that allows visitors to browse retired racehorses available for visits at registered ranches, and book a visit with a horse they are interested in.

## Project Purpose

Many retired racehorses are rehomed to ranches and farms. This platform connects horse lovers with those farms, allowing them to discover available horses and schedule a visit — while giving farmers a simple tool to manage their horses and bookings.

---

## User Roles

### Guest (Not Logged In)
- Browse all available horses across all farms
- View horse detail pages (name, breed, age, background story)
- View farm profiles
- Search and filter horses

### Visitor (Logged In)
Everything a guest can do, plus:
- Book a visit to see a specific horse using a calendar
- View and manage their own bookings
- Cancel a booking

### Farmer
- Register their farm (name, location, description, photos)
- Add, edit, and remove horses from their farm
- View incoming booking requests
- Approve or reject bookings
- Mark visits as completed

### Admin *(planned for future)*
- Manage all users and farms
- Handle disputes or reports
- View platform-wide statistics

---

## Core Features

### Horse Browsing
- Public list of all available horses
- Horse detail page with info: name, breed, age, color, backstory
- Search by name, breed, or farm
- Filter by availability

### Booking System
- Calendar-based booking for logged-in visitors
- Booking status flow: `Pending → Approved → Completed / Cancelled`
- Conflict prevention — same horse cannot be double-booked on the same date
- Booking history for visitors
- Booking management dashboard for farmers

### Farm Registration
- Farmers can register and manage their own farm profile
- Each farm can have multiple horses

### Authentication & Authorization
- Register and login system
- Role-based access control (Guest, Visitor, Farmer, Admin)
- Protected routes — booking and farm management require login

---

## Suggested Tech Stack

### Frontend
- React + React Router
- Tailwind CSS
- Calendar UI library (e.g. react-calendar or react-big-calendar)

### Backend
- Node.js + Express (or Fastify)
- JWT-based authentication
- bcrypt for password hashing

### Database
- PostgreSQL (relational — fits users → farms → horses → bookings well)

---

## Data Models (Draft)

```
User        — id, name, email, password, role (visitor | farmer | admin)
Farm        — id, owner_id, name, location, description
Horse       — id, farm_id, name, breed, age, color, bio, is_available
Booking     — id, horse_id, visitor_id, date, status (pending | approved | completed | cancelled)
```

---

## Build Order (Recommended)

1. Auth system — register, login, roles
2. Farmer flow — register farm, add horses
3. Guest flow — browse and search horses
4. Visitor flow — calendar booking
5. Admin panel *(future)*

---

## Why This Project

- Real-world scheduling problem (calendar + conflict logic)
- Role-based access control across multiple user types
- Clear business purpose — easy to explain in interviews
- Memorable concept that stands out from generic CRUD apps
