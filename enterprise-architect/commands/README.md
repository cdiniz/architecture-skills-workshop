# Commands

Slash commands for the `enterprise-architect` plugin live here.

Each command is a single Markdown file — the filename becomes the command name
(`review-design.md` → `/review-design`). The file body is the prompt that runs
when the command is invoked; optional YAML frontmatter can set a `description`
and an `argument-hint`.

Example (`commands/review-design.md`):

```markdown
---
description: Review a design document against our architecture principles
argument-hint: <path-to-design-doc>
---

Review the design at $ARGUMENTS against our architecture principles. For each
principle, state whether the design upholds it and cite the relevant section.
```

Delete this README once you add real commands.
