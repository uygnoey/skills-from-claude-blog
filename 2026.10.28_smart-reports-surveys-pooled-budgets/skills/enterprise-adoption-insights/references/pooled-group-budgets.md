# Pooled group budgets

Summary of what the source says. Setup details: the Help Center article "Manage pooled group budgets on
Enterprise plans" (https://support.claude.com/en/articles/17005973-manage-pooled-group-budgets-on-enterprise-plans).

## Why
Heavy users are less likely to hit an individual limit early in the month while others leave budget unspent,
because the group shares one monthly budget.

## How the two limits interact
| Limit | Role |
|---|---|
| Pooled group budget | One shared monthly amount for the whole group |
| Member limit | Guardrail against unusually high individual use |

- Every request counts against **both**.
- A member stops at **whichever runs out first**.

## Raising limits
- A member who hits a limit can request more from inside Claude.
- The request goes to admins for review.

## Setup and alerts
- Setup suggests an amount based on the group's recent usage.
- Admins with billing permissions get email alerts at **50%, 75%, 95%, and 100%** of a budget.

## Worked check (illustrative numbers, not from the post)
| Group budget left | Member limit left | Next request |
|---|---|---|
| Plenty | Plenty | Runs |
| Plenty | Exhausted | Stops - member limit reached; member can request more |
| Exhausted | Plenty | Stops - group budget reached |
