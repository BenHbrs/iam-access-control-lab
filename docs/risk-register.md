# Risk Register (MVP)

| Risk | Impact | Likelihood | Control / Mitigation | Owner |
|------|--------|------------|----------------------|-------|
| Unauthorized access to /admin | High | Medium | RBAC admin role required | Dev |
| Token theft / leakage | High | Low | Do not store tokens in repo; short-lived tokens | Dev |
| Missing audit trail | Medium | Medium | Write audit logs for all requests | Dev |
| Misconfigured roles | Medium | Medium | Document roles and test access paths | Dev |
| Dependency vulnerabilities | Medium | Medium | Pin versions / update regularly | Dev |
