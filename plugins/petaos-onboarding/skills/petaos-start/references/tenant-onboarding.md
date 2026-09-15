# Registered tenant onboarding

Use this guide when the customer already has a PETAOS tenant and wants to understand available capabilities, train users, or receive help completing an authorized task.

## Establish tenant context

Use information the customer already supplied and collect only what changes the training or operation:

- Confirm the current tenant/environment and the user's role. Let the user complete login, MFA, or third-party authorization.
- Read the applications and menus visible in the current session. Do not infer access from the full plugin catalog.
- Identify the user's job outcome and current level: new user, occasional operator, administrator, or process owner.
- Agree on the service level: explanation, guided practice, or execution. Training defaults to read-only; write operations require explicit scope.

## Explain what the tenant can do

Create a capability map from the live tenant, grouped by the customer's role and workflow rather than by every available menu. For each relevant capability, state:

1. What business result it supports.
2. Which PETAOS module and entry point it uses.
3. Required role, master data, configuration, or integration.
4. The normal workflow and important status transitions.
5. How completion is verified and which downstream module receives the handoff.

Mark each capability as **available**, **permission required**, **configuration required**, **not enabled**, **error**, or **pending verification**. A visible menu alone is not proof that the feature is usable.

## Train and help the customer

1. Select no more than three high-frequency tasks for the user's role.
2. Read only the matching module skill and task card. Explain why the task matters, what data is needed, each step, and completion evidence.
3. Demonstrate with approved sample data when a test environment exists. Otherwise remain read-only or use manual guidance.
4. For guided practice, let the customer perform each consequential action and verify the resulting state together.
5. For authorized execution, use the host browser to open the real page, read current labels, perform only the approved actions, and re-query the saved record. Obtain specific confirmation before publishing, sending, paying, approving, signing, or changing access.
6. Record the task, role, environment, result, evidence, error, and next action without retaining credentials or unnecessary personal data.

Without browser control, provide the exact page, visible label to find, field purpose, expected state, and the sanitized result the user should return. Never claim that the plugin opened or changed the tenant.

## Improve efficiency

Recommend improvements only after understanding the current workflow. Prefer the smallest change that removes a real bottleneck:

- Reuse approved master data and templates instead of repeated entry.
- Connect module handoffs so order, inventory, payment, production, and accounting status do not need manual reconciliation.
- Standardize approval conditions and keep human confirmation for consequential actions.
- Use saved views, batch actions, notifications, or AI assistance only when the current tenant visibly supports them.
- Compare before/after measures such as handling time, duplicate entries, waiting time, exception count, or reconciliation effort; do not promise an unmeasured percentage gain.

## Completion evidence

Return a tenant capability map, role-based training plan, completed task evidence, blocked or unavailable items, and the next one-to-three recommended tasks. Distinguish clearly between explained, demonstrated, customer-completed, and assistant-executed work.
