# GovScheme API Endpoint List
## Status: Draft (Week 1/2) — to be reviewed and locked at Architecture Freeze

| Method | Path | Purpose | Auth |
|---|---|---|---|
| POST | /api/v1/auth/register | Create a new user account | Public |
| POST | /api/v1/auth/login | Log in, returns JWT | Public |
| POST | /api/v1/profile | Create/update the caller's profile (upsert) | Authenticated |
| GET | /api/v1/profile | Get the caller's own profile | Authenticated |
| GET | /api/v1/locations/states | List all states | Authenticated |
| GET | /api/v1/locations/districts?stateId={id} | List districts for a state | Authenticated |
| GET | /api/v1/locations/talukas?districtId={id} | List talukas for a district | Authenticated |
| GET | /api/v1/locations/localities?talukaId={id} | List localities for a taluka | Authenticated |
| GET | /api/v1/schemes/{id} | Get full scheme details | Authenticated |
| GET | /api/v1/schemes/eligible | Get schemes the caller is eligible for | Authenticated |
| GET | /api/v1/recommendations | Get AI-ranked, explained scheme recommendations | Authenticated |
| POST | /api/v1/applications | Mark a scheme as applied | Authenticated |
| GET | /api/v1/applications | List the caller's own tracked applications | Authenticated |
| GET | /api/v1/notifications | List the caller's notifications | Authenticated |
| GET | /api/v1/admin/schemes | List all schemes (including Draft/Archived) | Admin only |
| POST | /api/v1/admin/schemes | Create a new scheme | Admin only |
| PUT | /api/v1/admin/schemes/{id} | Update a scheme | Admin only |
| DELETE | /api/v1/admin/schemes/{id} | Delete a scheme | Admin only |
| PATCH | /api/v1/admin/schemes/{id}/verify | Transition PENDING_VERIFICATION → ACTIVE | Admin only |
| GET | /api/v1/admin/audit-logs | View audit log history | Admin only |