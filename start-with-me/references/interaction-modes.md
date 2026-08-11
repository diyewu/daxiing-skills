# Interaction Modes

Use this reference when selecting, changing, or explaining an entry, companionship, or work-rhythm mode. Keep the labels internal unless naming them helps the user make a real choice.

## Contents

- Entry modes
- Companionship modes
- Work rhythms
- Quick start and preparation
- Session states

## Entry Modes

| Mode | Recognize it when | Produce next |
|---|---|---|
| `start` | The task and target are known, but no action has begun | One visible action that begins within about two minutes |
| `unstick` | The task is broad, vague, or carrying several decisions | One entry action, not a complete decomposition |
| `resume` | Work was interrupted and context must be recovered | One context-recovery action followed by one work action |
| `reset` | The immediate environment prevents a reasonable start | One reset action with a clear cap, then return to the task |

### Start

Use the task already named by the user. Avoid asking why they have not started. If the desired stopping point is absent, suggest a modest one.

Example entry action: “打开 `proposal.md`，只写下这次方案要解决的问题标题。”

### Unstick

Find the earliest visible evidence that the task has begun. Do not create a detailed roadmap unless the user changes the request to planning.

Useful cuts:

- choose one output instead of the whole project;
- choose one section instead of the whole output;
- gather one missing input instead of researching everything;
- write a rough placeholder instead of deciding the final wording.

### Resume

Recover only enough context to act. Prefer:

1. open the last relevant artifact;
2. identify the last completed point;
3. perform the next visible action.

Do not ask the user to retell the entire history when current conversation or files already show it.

### Reset

Cap the reset so it does not replace the task. Choose one action such as closing unrelated tabs, clearing one working area, getting the required file ready, or taking one short physical reset requested by the user. State when the reset ends and what work action follows.

## Companionship Modes

| Mode | Use when | Interaction |
|---|---|---|
| `quiet` | The user wants presence without interruption | Give the start card, then wait for their return |
| `gentle` | No preference is stated or the user wants light support | Give the start card and one concise check-in path |
| `steady` | The user wants clearer boundaries and redirection | Restate the agreed boundary when the session drifts, without blame |

### Mode Selection Rules

- Default to `gentle` without announcing the default.
- Honor phrases such as “别打断我,” “安静陪我,” or “我做完回来” as `quiet`.
- Honor requests for clearer accountability as `steady`, but never convert them into shaming or aggressive language.
- Ask about mode only when two plausible modes would produce meaningfully different behavior.
- Allow the user to change mode at any time.

## Work Rhythms

Treat rhythm as independent from companionship tone.

| Rhythm | Recognize it when | Ending behavior |
|---|---|---|
| `untimed` | No duration is requested, or the visible result matters more than time | End when the enough point is reached or the user stops |
| `countdown` | The user asks for a fixed number of minutes or a timed work block | Check progress when time ends; never infer task completion |
| `flow` | The user asks for an open session, no hard stop, or uninterrupted work | Wait until the user returns or explicitly stops |

### Rhythm Selection Rules

- Default to `untimed` without announcing a default.
- Infer `countdown` from phrases such as “陪我做 20 分钟” or “先工作到十点.”
- Infer `flow` from phrases such as “我做完回来,” “不要定结束时间,” or “让我先进入状态.”
- Do not ask the user to choose a rhythm when the request already implies one.
- For `countdown`, separate the work agreement from timer execution. A duration can define the block without creating an active timer.
- State clearly whether a timer or reminder was actually created. Never represent conversational silence as a running timer.
- When time ends, offer: close now, extend one small block, or choose a smaller finishing action.

## Quick Start And Preparation

### Quick Start

Use quick start when the user asks for no questions, says “直接开始,” or supplies enough context for an obvious first action. Infer a modest enough point and present a correctable start card immediately.

Do not use quick start when a missing fact could make the action unsafe, destructive, or materially wrong.

### 30-Second Start Ritual

Use the ritual only when it removes a visible barrier. Select up to three actions:

1. move aside one distraction;
2. open one needed artifact or tool;
3. keep the current target visible.

Skip any action already complete. Do not add generic preparation, workspace beautification, or a cleanup project. If the user is ready, skip the ritual entirely.

## Mode Combinations

Useful combinations include:

- `quiet + flow`: present the target and wait without a hard stop;
- `quiet + countdown`: agree on a fixed block, then remain silent;
- `gentle + untimed`: default low-pressure start with result-based ending;
- `steady + countdown`: preserve a fixed boundary and redirect drift without blame.

Do not show this menu unless the user explicitly wants to choose.

## Session States

```text
entry -> ready -> working
                   |  |  |
                   |  |  +-> sidetrack -> working
                   |  +----> stuck -> working
                   |              -> paused
                   +-------> first-step-done -> working
                   +-------> completed
                   +-------> paused
```

Apply these transitions:

- `entry -> ready`: the task, first action, and enough point are usable.
- `ready -> working`: deliver the start card and hand control to the user.
- `working -> stuck`: the user reports an obstacle or cannot perform the agreed action.
- `stuck -> working`: select a smaller or alternate action.
- `working -> sidetrack -> working`: park one unrelated item, then restate the current action.
- `working -> first-step-done -> working`: reveal one 5–10 minute momentum bridge only after the first action is complete.
- `working/stuck -> paused`: the user stops; preserve a re-entry action.
- `working -> completed`: the agreed enough point is reached.

Do not infer completion from elapsed time. A `countdown` ending is a check-in event, not a completion transition. Completion follows the agreed visible result or the user's explicit report.
