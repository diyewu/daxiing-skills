# Activity Decision Framework

## Contents

- Decision modes
- Constraint model
- Candidate generation
- Hard filters
- Ranking
- Alternatives
- Decision cards
- Common failure patterns

## Decision Modes

### Quick Pick

Use when context is sufficient or the user explicitly wants no questions.

Output one plan. Add one fallback only when a known uncertainty could block the first plan, such as weather, sold-out tickets, transport, or venue closure.

State material assumptions briefly:

> 我先按“市区内、两小时、每人 100 元以内”替你选；有一项不对，直接改那一项。

Do not disguise missing location or safety-critical information as an assumption.

### Compare

Use when the user asks to compare or when distinct tradeoffs matter.

Give no more than three options. Each option must own a different reason to choose it, for example:

- lowest friction;
- lowest cost;
- most active;
- best for uncertain weather;
- easiest with children or accessibility needs.

Do not provide three variants of the same venue category unless the user explicitly wants venue comparison.

### Shape It

Use when one missing fact changes the recommendation class, feasibility, safety, or cost.

Ask one question. Prefer compact choices only when they reduce effort:

> 你们今晚更想待在家，还是可以出门半小时以内？

Avoid asking for mood, budget, group, location, time, food, alcohol, and energy in one survey. If two facts are missing, ask for the most constraining one, then propose a plan with a stated assumption for the other.

## Constraint Model

### Time

Resolve:

- start window;
- total available duration;
- deadline or last transport if relevant;
- immediate versus future plan.

Do not suggest a two-hour activity when only 45 minutes are available after travel and setup.

### Place And Movement

Resolve only the minimum useful precision:

- at home;
- city or district;
- travel radius or maximum travel time;
- walking, public transit, driving, or no preference.

Ask for an exact address only when a real tool needs it for a user-approved action.

### People

Resolve:

- solo, pair, family, or group;
- group size;
- children, minors, or pets when stated;
- differing constraints that affect feasibility.

Do not request names or contact details for activity selection.

### Budget

Use a total or per-person range when available. Include likely transport, tickets, food, equipment, or materials if they are material.

If current prices are not verified, label the amount as an estimate or use a broad band. Do not convert invented confidence into exact currency.

### Energy And Intensity

Map the user's words to practical levels:

- very low: minimal setup and movement;
- relaxed: light movement, easy conversation;
- moderate: sustained activity without special preparation;
- active: physical activity, equipment, or meaningful travel.

Do not infer health or fitness. An intensity preference is not medical clearance.

### Hard Constraints

Treat these as filters before ranking:

- accessibility;
- dietary restrictions or allergies;
- age restrictions and supervision;
- weather exposure;
- transport and driving limits;
- pets;
- alcohol preference;
- explicit dislikes;
- cost ceiling;
- safety alerts.

Never let novelty or a “surprise” mode override a hard constraint.

## Candidate Generation

Generate a small private pool across only relevant categories:

- simple home activity;
- food or cooking experience;
- game, film, performance, or creative activity;
- walk, park, sport, or outdoor activity;
- local class, exhibition, market, or event;
- low-friction social ritual.

The list is a thinking aid, not an output requirement. Do not browse categories that the user's constraints already exclude.

## Hard Filters

Reject a candidate when:

- it violates a stated constraint;
- its setup plus travel cannot fit the available time;
- likely cost exceeds the ceiling;
- live availability is necessary but cannot be verified and no safe caveat makes it useful;
- it creates a foreseeable weather, transport, age, dietary, or accessibility problem;
- it depends on equipment or participants the user does not have;
- it is merely a work task disguised as leisure.

## Ranking

Rank viable candidates in this order:

1. feasible now;
2. satisfies hard constraints;
3. low setup and travel friction;
4. fits time and budget;
5. tolerates uncertainty;
6. fits the desired energy and social context;
7. adds useful novelty.

The top choice should be the easiest good decision, not the most impressive idea.

## Alternatives

An alternative is useful only if it protects against a different risk or preference.

Good fallback reasons:

- weather turns bad;
- tickets are gone;
- the group wants lower cost;
- energy drops;
- leaving home becomes inconvenient.

Do not add a wild card by default. A surprising option is appropriate only when the user asks for novelty and it still meets all hard constraints.

## Decision Cards

### Local Plan

```text
今天就选：活动与地点
为什么合适：用两项关键约束解释
怎么开始：第一个动作
时间与预算：核验值或清楚标记的估计
出发前确认：仍有变化风险的事实
备选：解决一个不同取舍
```

### Home Plan

```text
今晚就做：具体活动
为什么合适：人数、时间、精力或已有材料
准备：不超过三项
玩法：简短的开始规则
做到这里就够：一个自然结束点
```

### Comparison

Use a compact table only when three repeated fields materially help:

| 方案 | 适合原因 | 时间 | 预算 | 主要取舍 |
|---|---|---:|---:|---|

After the table, recommend one option. Do not leave the user with an unranked list.

## Common Failure Patterns

### The Survey

Asking every possible preference before producing value. Fix it by asking only the most decision-changing question.

### The Search Dump

Returning ten venues or activities without choosing. Fix it by filtering, ranking, and stating one recommendation.

### False Specificity

Adding exact prices, ratings, hours, or travel times without verification. Fix it by verifying or labeling estimates.

### Decorative Personalization

Mentioning weather or group context without changing the plan. Include context only when it affects the decision.

### Novelty Over Feasibility

Choosing an impressive idea that is expensive, far away, inaccessible, or hard to start. Re-rank feasibility first.

### Endless Planning

Continuing to optimize after the user accepts a feasible idea. Preserve the choice and give the next action.
