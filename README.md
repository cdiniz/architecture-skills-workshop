# architecture-skills-workshop

Scaffolding for a Claude Code plugin used in a hands-on workshop.

The workshop is about **architects building their own skills and tooling** for
their function — turning the things they do repeatedly (writing ADRs, modelling
systems, assessing trade-offs, reviewing designs against principles) into
reusable Claude Code skills, commands, and agents.

This repository gives participants a ready-to-extend starting point so they can
focus on authoring skills rather than wiring up plumbing.

## What's here

- `.claude-plugin/marketplace.json` — the marketplace manifest. It publishes a
  single `enterprise-architect` plugin (sourced from `./enterprise-architect`)
  that participants flesh out during the workshop.

## How it's used in the workshop

1. Install the marketplace and the `enterprise-architect` plugin.
2. Scaffold the plugin under `./enterprise-architect` (a `.claude-plugin/plugin.json`
   plus `skills/`, `commands/`, and `agents/` directories).
3. Author skills and tooling for common architecture tasks — for example ADRs,
   C4 modelling, quality-attribute assessment, or design review.
4. Reload plugins and iterate on the skills against real work.

> The `./enterprise-architect` plugin directory is intentionally left empty —
> building it out is the exercise.
