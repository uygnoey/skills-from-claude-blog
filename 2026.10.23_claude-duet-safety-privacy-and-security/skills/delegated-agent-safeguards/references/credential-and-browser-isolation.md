# Credential and browser isolation

The principle: the model works with the user's accounts without ever seeing their secrets.

## Passwords
- The user types the password into a form in the app, not into the chat.
- It is encrypted with a single-use key.
- The browser machine types it into the site. The model never sees it.
- The post says a 1Password integration is planned.

## Sign-in tokens
- The agent works with placeholders instead of real tokens.
- A proxy outside the agent's machine inserts the real values into requests as they go out.

## Browser
- Runs in a dedicated cloud virtual machine, separate from the agent.
- The agent drives it only through a fixed set of commands.
- Site code and cookies stay on the browser machine.
- Page text and downloads do come back to the agent, so they remain untrusted input (see the intent check
  and outgoing-message classifier in the skill).

## Identifying the agent
- A distinct User-Agent header.
- Published IP addresses.
- Some websites have chosen to block it.

## Payments
- One-time card from a wallet service (Link from Stripe), limited to one merchant and one amount.
- The user's real card number is not shared.
