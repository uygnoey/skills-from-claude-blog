---
name: agentic-coding-adoption-playbook
description: A practical playbook for rolling out agentic coding across an engineering organization: piloting, enablement, guidance, and measurement.
---

## Instructions
Use this skill to plan and execute an organization-wide rollout of agentic coding tools.

1. **Define target use cases** (e.g., modernization, onboarding, incident response) and where you expect leverage.
2. **Start with a pilot cohort** of experienced “super users” who can develop internal practices.
3. **Standardize guidance** with project-level documentation (for example, a repository-root CLAUDE.md) and keep it updated via normal code review.
4. **Enable the broader org** via workshops, internal champions, and shared examples.
5. **Scope work incrementally** (tests-first when appropriate) to reduce risk and make progress measurable.
6. **Request complete context** when diagnosing issues: full errors, environment details, expected vs actual behavior, and relevant files.
7. **Measure impact** using both delivery outcomes (throughput, cycle time) and usage/acceptance metrics where available.


## Examples
- Write tests for user registration, then implement the registration logic to pass these tests.
- Build a REST API for user management, including specific endpoints and requirements.
- Optimize the database query to reduce response time from 2 seconds to under 500ms.
- Follow this existing API pattern [paste code] / Use this coding style [share guide].
- Create the database schema → implement product catalog API → add shopping cart functionality.
- Create a basic user login form → add input validation → implement password strength requirements.
- The error handling is too generic—add specific validation for email format and password length.
- Using the authentication middleware from earlier, now add role-based permissions.
