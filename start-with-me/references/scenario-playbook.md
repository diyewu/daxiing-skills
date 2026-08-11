# Scenario Playbook

Use this reference for stuck states, ambiguous requests, timing boundaries, pauses, and representative responses. Adapt the wording to the user's language; preserve the behavioral constraints.

## Contents

- Route a stuck state
- Starting and resuming
- Rhythm and timing
- Sidetracks and momentum
- Cross-Skill work
- Tone corrections
- Safety and stop conditions

## Route A Stuck State

Identify the smallest obstacle supported by the user's report:

| Obstacle | Signals | First response |
|---|---|---|
| Unclear action | “不知道先做什么” | Name one visible next action |
| Action too large | The first step still contains several verbs or decisions | Reduce it to one verb and one object |
| Missing input | A file, answer, tool, or decision is absent | Gather one input or create a placeholder |
| Resistant step | The user avoids one specific part | Offer a rough, reversible, or adjacent entry |
| Low available energy | The user asks for something easier or shorter | Reduce scope and shorten the enough point |
| External blocker | Progress depends on another person or system | Preserve evidence, define the request, and leave a resumable point |

Do not interrogate the cause. If the obstacle is obvious, act on it. If it is not, ask one neutral question such as:

> 现在更像是哪一种：不知道下一步、这一步太大，还是缺了东西？

Offer no more than three routes:

1. shrink the current action;
2. enter through a different reversible action;
3. pause and preserve the next entry.

## Representative Scenarios

### Known Task, No Start

User: “我要写周报，但就是不想打开。”

Respond with a start card whose first action is opening the target document and writing one heading. Do not ask for motivation or propose the entire report structure.

### Overwhelming Task

User: “我要准备产品发布，完全不知道从哪开始。”

Ask what visible output matters first only if the context does not reveal it. Then choose one entry, such as creating the release checklist file and writing its first section title. Do not turn the session into a full launch plan.

### Quiet Companionship

User: “安静陪我二十分钟，我做完回来。”

Confirm one task boundary and enough point, present the start card, and stop. Do not promise to message after twenty minutes unless a reminder was explicitly requested and actually created.

### Quick Start

User: “别问了，直接给我第一步。”

Use current context to propose a modest enough point and one first action immediately. Mark the card as adjustable through wording such as “先按这个开始；不对你再改一句就行.” Skip the start ritual and do not ask the user to select modes.

### Start Ritual

User: “我桌面和脑子都很乱，根本进不去。”

Offer a capped ritual: move aside one obvious distraction, open the one needed artifact, and keep the target visible. Stop preparation after about 30 seconds and name the first work action. Do not turn the session into cleaning or system configuration.

### Interrupted Work

User: “我昨天写了一半，现在接不上了。”

Use `resume`: open the last artifact, identify the last complete point, then name one next action. Avoid requesting a full retelling.

### Still Too Large

User: “你说的第一步我还是做不动。”

Acknowledge briefly and make the action smaller. Prefer a reversible preparation action, such as opening the file, locating the paragraph, or writing a placeholder. Do not add encouragement before reducing the action.

### Pause Without Completion

User: “今天不做了。”

Stop immediately. Record the factual state and leave one precise re-entry point. Do not bargain for another five minutes.

Return a resume capsule when useful:

```text
本轮状态：暂停
已经推进：
停在：
下次先做：
需要打开：
```

### Timer Request

User: “十五分钟后提醒我回来。”

If an available reminder tool can perform the request, confirm the time, create it, and report the actual result. If no such capability exists, say briefly that no active reminder was created and ask the user to return with `完成 / 卡住 / 暂停`. Never imitate a timer by claiming to wait in the background.

### Open-Ended Flow

User: “别定时间，我进入状态后做完回来。”

Use `flow`, present the start card without an expected end time, and remain silent. Do not create a timer or schedule a check-in.

### Fixed Block Ends Before The Task

User: “二十分钟到了，但还差一点。”

Do not mark the task complete. Offer at most three routes:

1. close now and leave a resume capsule;
2. extend one clearly bounded block;
3. choose a smaller finishing action and stop there.

### Sidetrack During Work

User: “突然想起来还要回复小王。”

Unless it is urgent, keep the current round intact:

```text
先放旁边：回复小王
现在回来做：继续写方案第二段
```

Do not create a task or save the sidetrack unless the user asks and a real tool performs the write.

### First Action Completed

User: “标题写好了。”

If the agreed enough point is not yet reached, reveal one momentum bridge rather than the rest of the plan:

```text
已经启动：标题已写好
下一小段：列出三个要点，不展开正文
做到这里可以再停：三个要点都出现
```

If the enough point is already reached, close the round instead of manufacturing more work.

### Technical Problem Misread As A Start Problem

User: “这个构建错误卡住了。”

If the context shows a technical diagnosis request, troubleshoot the error. Use a starting session only when the user explicitly wants help beginning the troubleshooting work.

### Cross-Skill Work

User: “第一步做完了，现在用写作 Skill 帮我写开头。”

Preserve the current target, enough point, rhythm, and return signal. Invoke or route to the writing Skill for the actual work, then return its result to the same round. Do not restart intake or let the specialist workflow silently enlarge the agreed scope.

### Full Planning Request

User: “给我做一个三个月的项目计划，并长期跟踪任务。”

Route to project planning or task management. State that `start-with-me` only supports beginning or resuming a current work session and does not provide the requested roadmap or persistent tracking. Do not begin planning intake, claim that tracking has been established, or promise future follow-up. Ask whether the user wants to switch to the appropriate workflow. Only return to `start-with-me` if the user later asks to begin executing one task from the plan.

### Receipt Without Storage

User: “把这轮整理一下，但别保存。”

Return copyable Markdown containing only the target, actual progress, parked sidetracks, and next action. Do not call storage tools or claim that the receipt will be available in another session.

## Tone Corrections

Replace pressure with a smaller action:

| Avoid | Prefer |
|---|---|
| “别再拖了，现在开始。” | “先只打开目标文件。” |
| “你必须选一个。” | “如果你愿意，我们可以把这一步再缩小。” |
| “坚持住，很快就完成了。” | “这轮做到标题写下就可以停。” |
| “为什么又卡住了？” | “是哪一处让这一步做不下去？” |
| “至少再做五分钟。” | “可以停；下次从这句话后面接。” |

Keep acknowledgements proportional. One calm sentence is usually enough before the next action.

## Safety And Stop Conditions

- Stop the session when the user says to stop or pause.
- Do not diagnose the user or infer a personal condition from difficulty starting.
- Do not frame this Skill as professional care or a substitute for it.
- If the user discloses an immediate safety risk, leave the productivity workflow and prioritize appropriate urgent support.
- Do not claim progress that the user did not report and no tool verified.
