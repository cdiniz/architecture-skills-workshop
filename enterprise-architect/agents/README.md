# Agents

Subagents for the `enterprise-architect` plugin live here.

Each agent is a single Markdown file with YAML frontmatter defining `name`,
`description`, and (optionally) the `tools` it may use and the `model` to run on.
The body is the agent's system prompt.

Example (`agents/principle-reviewer.md`):

```markdown
---
name: principle-reviewer
description: Reviews designs and code changes against enterprise architecture principles and flags violations.
tools: Read, Grep, Glob
---

You are an enterprise architecture reviewer. Given a design or diff, check it
against the organisation's architecture principles and report any violations
with the principle name, the location, and a suggested remediation.
```

Delete this README once you add real agents.
