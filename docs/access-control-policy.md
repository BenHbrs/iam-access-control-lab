# Access Control Policy (MVP)

## Purpose
Define access control rules for this lab project using least privilege.

## Principles
- Least privilege
- Role-based access control (RBAC)
- Separation of duties
- Logging & monitoring for access events

## Roles
- user: can access /user
- admin: can access /admin

## Authentication
OIDC via Keycloak (JWT tokens)

## Authorization
RBAC based on roles inside the token (realm_access.roles)

## Logging
API logs access attempts with user, endpoint, status, timestamp.
