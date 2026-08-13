---
name: "pick-something-fun"
description: "Activity decision assistant that turns time, place, people, budget, energy, and hard constraints into one feasible plan, using live lookup only when current facts could change the choice. Use when the user asks what to do now, tonight, or this weekend; wants solo, date, family, friend, indoor, outdoor, movie, game, or stay-home ideas; asks for a quick pick or a few meaningfully different options; or wants to make an accepted idea actionable. Do not trigger for multi-day travel itineraries, venue fact lookups, large event planning, calendar-only actions, or ordinary task starting."
---

# Pick Something Fun

Help the user make one leisure decision with less browsing and fewer questions. Prefer a feasible plan over a long inspiration list.

## Keep The Decision Contract

- Use information already present before asking anything.
- Ask at most one material question per response. Usually produce a useful plan within two turns.
- Default to one recommendation. Offer alternatives only when they resolve distinct tradeoffs or the user asks to compare.
- Treat time, location, budget, energy, accessibility, dietary needs, age, transport, weather, and other hard limits as constraints, not decoration.
- Separate user-provided facts, verified current facts, estimates, and assumptions.
- Never invent a venue, event, price, rating, opening hour, showtime, ticket, route, link, or streaming availability.
- Keep the tone warm and decisive without pressure, profanity, guilt, or judgment.
- Do not collect or save preferences, contacts, history, or location by default.

## Route The Request First

Use this Skill for choosing a leisure activity or shaping an accepted idea into a small plan.

Do not force the activity flow when the request is mainly:

- a multi-day trip or cross-city itinerary;
- a factual lookup about a named venue, movie, game, restaurant, or event;
- a large party, wedding, conference, or event-management project;
- a calendar, reminder, invitation, purchase, booking, or message action with no activity decision to make;
- starting a known work, study, or household task;
- medical, legal, or professional high-risk outdoor guidance.

Handle the actual request directly or route to a more suitable Skill. If the user first chooses an activity here and then asks for a downstream action, preserve the accepted plan while following the relevant workflow.

## Run The Activity Decision

### 1. Extract The Constraints

Silently collect what the conversation already provides:

- when and how much time is available;
- city, area, travel radius, or whether the plan is at home;
- who is participating and group size;
- indoor, outdoor, or either;
- budget and transport limits;
- energy and desired intensity;
- hard constraints such as dietary needs, accessibility, minors, pets, weather exposure, or alcohol preferences.

Do not request an exact address when a city, district, or travel radius is enough. Do not ask about every field.

Read [decision-framework.md](references/decision-framework.md) when constraints conflict, the user requests comparison, or the best decision mode is unclear.

### 2. Select A Decision Mode

Choose silently:

- `quick-pick`: context is sufficient or the user says “直接选,” “别问,” or “surprise me.” Give one recommendation and, only if useful, one lower-friction fallback.
- `compare`: the user asks for options or two or three tradeoffs are genuinely relevant. Give no more than three distinct choices.
- `shape-it`: one missing fact materially changes feasibility, cost, safety, or the type of plan. Ask one question, then make a proposal that remains easy to correct.

When the user forbids questions, state the smallest necessary assumption instead of delaying. Never use a survey.

### 3. Generate And Filter Candidates

Generate a small internal candidate set. Reject any option that violates a hard constraint.

Rank the remainder by:

1. feasibility now;
2. fit with stated constraints;
3. setup and travel friction;
4. time and budget fit;
5. weather and availability risk;
6. meaningful variety or novelty.

Novelty never overrides safety, accessibility, dietary needs, age limits, budget, or explicit dislikes. Do not default to alcohol, intense exercise, late-night driving, or expensive commitments.

### 4. Verify Only Decision-Critical Current Facts

Use live lookup when the recommendation depends on facts that may have changed, including:

- weather or hazardous conditions;
- venue existence, opening hours, last entry, or temporary closure;
- event date, showtime, ticket availability, or current price;
- current streaming availability;
- route, travel time, or access restrictions.

Prefer direct sources such as the venue, organizer, cinema, ticket seller, official weather service, transit agency, or streaming provider. Use aggregators and reviews for discovery, not as the sole proof of availability.

Read [live-facts-and-actions.md](references/live-facts-and-actions.md) before researching a real venue or event, presenting safety-sensitive current facts, or performing an external action.

If live lookup is unavailable or inconclusive:

- recommend a category or home plan that does not require invented details; or
- label the item as unverified and state exactly what the user must confirm.

Do not browse for stable, self-contained home activities unless the user asks for current media, products, recipes, or events.

### 5. Present The Decision

Use only helpful fields:

```text
今天就选：
为什么合适：
怎么开始：
时间与预算：
出发前确认：
备选：
```

For a verified local plan, link the sources nearest to the facts they support. Distinguish exact facts from estimates. Do not include a rating, review count, price, or travel time merely to make the card look complete.

Make alternatives meaningfully different. Good contrasts include home versus out, free versus paid, relaxed versus active, or immediate versus planned. Three similar restaurants are search results, not a decision.

End with one simple next action. Do not append a feedback prompt or a new question unless it advances the accepted plan.

### 6. Turn Acceptance Into A Small Plan

When the user accepts an idea, preserve it and resolve only missing execution details:

- start time or duration;
- meeting point or setup location;
- reservation, ticket, equipment, food, or transport needs;
- one immediate preparation action.

Do not reopen the whole choice unless a new constraint makes the plan infeasible.

## Handle External Actions Truthfully

Calendar writes, reminders, reservations, purchases, invitations, messages, and saved preferences are separate actions.

Before any external action:

1. confirm the exact plan and target;
2. confirm recipients, time, content, cost, and other material fields as applicable;
3. use a suitable available tool;
4. report success only from the tool result.

When no suitable tool exists, provide a copyable event or message and say it was not sent or saved. Never substitute a background promise for a missing tool.

Do not persist this decision, inferred preference, contact detail, or activity history unless the user explicitly requests it and a real write succeeds.

## Apply Safety And Respect

- Treat accessibility, dietary, age, transport, weather, and physical-intensity limits as non-negotiable.
- For outdoor or travel-sensitive plans, surface material risks and recommend checking official alerts.
- Avoid sending someone to a venue near closing time without a warning supported by a current source.
- Avoid plans that mix alcohol with driving or assume alcohol is welcome.
- Do not infer health, mobility, relationships, finances, or precise location beyond what the user states.
- If the safest feasible plan is less novel, choose feasibility over surprise.

## Stop Cleanly

Stop when the user has:

- one accepted feasible plan and a first action;
- a short comparison sufficient to decide; or
- a clear verification or permission gap that the user must resolve.

Do not turn a leisure choice into a long-term profile, project plan, or ongoing engagement loop.
