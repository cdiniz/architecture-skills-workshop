---
name: stakeholder-finder
description: Given an issue, question, decision, or initiative, find the people in the organisation who should be consulted and explain how each one relates to it. Works on top of a stakeholder wiki — a repository of per-person markdown entries (frontmatter `type: stakeholder`, with Remit, Typical concerns, and Relationships sections). Use whenever the user asks "who should I talk to about X", "who are the stakeholders for this", "who owns / cares about / is affected by this", "who do I need to align with", "who should be in the room", or is scoping an architecture decision, migration, transformation programme, or change and needs to know whose input or sign-off matters — even if they don't say the word "stakeholder". Matches on responsibility AND concern AND organisational position, not just job title.
---

# Stakeholder Finder

The point of this skill is to answer a question every architect, programme lead, and
decision-maker asks constantly: **"given this issue, who do I actually need to talk
to?"** Not the whole org chart — the handful of people whose remit, concerns, or
position in the organisation make their input or sign-off matter for *this specific
thing*.

Getting this right saves people from two failure modes: missing someone who later
blocks or derails the work because they were never consulted, and over-inviting so
that the people who genuinely matter get diluted. So aim for a precise, justified
shortlist — relevance with a reason, not a directory dump.

## Where the stakeholder data comes from

This skill runs **on top of a stakeholder wiki**: a repository where each person is a
markdown file. You do **not** hardcode a path — the repository's own `CLAUDE.md` (or
equivalent context) tells you where the entries live and how they're organised. If
that context is already loaded, use it. If you can't tell where the entries are, find
them by their shape rather than guessing: they carry `type: stakeholder` in YAML
frontmatter and contain these sections:

- **Remit** — what the person is responsible for (their formal accountability).
- **Typical concerns** — what they worry about and advocate for (their lens).
- **Relationships** — line manager, functional/dotted-line leader, direct and
  functional reports, and `[[wiki-links]]` to other people.
- **Positions taken** / **Touches** — stances and topics/decisions they've engaged
  with, when populated from real meetings.

These three — **Remit, Concerns, Relationships** — are the three axes you match on.
A quick grep over the repo (e.g. for `type: stakeholder`) is the reliable way to be
sure you have the full set before you start reasoning.

## Workflow

### 1. Understand the issue, then ask a few check questions

Restate the issue in your own words so the user can correct you, then ask a **small**
number (usually 2–3) of short clarifying questions — and make them *grounded in what
the dataset actually distinguishes*, not generic project questions. The reason to
ask is that the same one-line issue ("data migration from AWS to Azure") can point at
very different people depending on details the user hasn't said yet: is regulated or
customer data in scope (pulls in compliance and data architecture), is it a one-off
or part of a standing transformation programme (pulls in the programme's people),
which domain's systems are moving (pulls in that domain's architect and tribe lead)?

Keep it light. If the user has already given enough to discriminate, or says "just
give me your best guess", skip ahead and surface your assumptions in the output
instead of interrogating them. The check questions are there to sharpen the
shortlist, not to gate it behind an interview.

### 2. Read all the entries and reason over three axes

Load **every** stakeholder entry — the set is small enough that reading all of them
beats keyword-filtering, and keyword-filtering is exactly how you miss the
non-obvious but important people. For each person, ask three separate questions:

- **Remit (responsibility):** Is this issue squarely within what they're accountable
  for? An owner who must act or sign off scores high on this axis.
- **Typical concerns (lens):** Does the issue touch something they actively worry
  about or advocate for, even if they don't own it? A person whose stated concern is
  "cross-border data transfer" is relevant to a cloud migration even if migration
  isn't in their remit.
- **Relationships (position):** Are they connected to the issue *structurally* —
  involved in a transformation programme the issue belongs to, the dotted-line
  functional leader for the discipline in play, or up/down the reporting chain from
  someone clearly central? This is the axis people forget, and it's often where the
  person who can unblock or escalate sits.

Most genuinely relevant people light up on more than one axis; that overlap is a
strong signal. Follow the `[[wiki-links]]` in the Relationships section when an
entry points you toward someone you'd otherwise have skipped.

A repository like this almost always links to people who have **no entry of their
own** — a manager, a functional leader, a programme sponsor named only as a
`[[wiki-link]]`. These are often genuinely important (the escalation/sign-off chain
usually lives here), but you only know their *position*, not their remit or
concerns. Keep them clearly separate from the people you can actually assess: a
linked name with no entry is a lead to follow up, not a stakeholder you can score.
See the next step for exactly where they go.

### 3. Score, filter, and explain

Score and rank **only people who have a real stakeholder entry** — those are the
only ones whose remit and concerns you've actually read. A person known only from a
`[[wiki-link]]` (no entry of their own) **never gets a score and never goes in the
ranked list**, no matter how structurally central they seem; scoring someone off an
inferred role is exactly the kind of fabrication that makes the whole shortlist less
trustworthy. They belong in the gap note instead (see Output format) so the user can
still act on them — typically by adding their entry and re-running.

Give each ranked person a **relevancy score from 1 to 10**, and **include only
people who are actually relevant** — if someone scores low, leave them out entirely
rather than padding the list. A good rough calibration:

- **8–10** — Central. Owns the issue or holds direct sign-off; the work can't really
  proceed without them.
- **5–7** — Should be consulted. A real stake via concern or domain overlap, or a
  structural/programme connection that makes their input or awareness matter.
- **1–4** — Marginal. Worth a mention only if the user wants to cast wide; usually
  omit.

Don't invent precision. The score is a judgement to help the user prioritise who to
approach first, not a measurement — so make the *rationale* carry the weight.

## Output format

Lead with a one-line read of the issue (including any assumptions you made), then list
the relevant stakeholders **ordered by score, highest first**. For each:

```markdown
### <Name> — <Role> · relevance <N>/10
<1–3 sentences: why they're relevant, naming which axis drives it — remit
(they own/sign off), concern (it touches their stated lens), or structural
(programme / dotted-line / reporting chain). If a specific concern or remit line
from their entry applies, cite it. Optionally end with what to ask them or align on.>
```

Then close with two short boundary notes, so the shortlist's edges are legible and
the user can catch a miss:

- **Deliberately left out** — profiled people you considered but didn't rank, and why
  (e.g. "Cloud Architect — relevant at build time, not for this decision").
- **Referenced but not in the wiki** — important-looking people who appear only as
  `[[wiki-links]]` with no entry (managers, functional leaders, programme sponsors).
  Name them and say why they'd matter, but **do not score them** — flag that their
  entry is missing and that adding it would let you place them properly. This is
  where the escalation/sign-off chain usually surfaces.

If your check questions went unanswered, state the assumptions the shortlist rests on
so the user can redirect you.

## Notes

- **Relevance needs a reason.** Never list a name without saying which axis makes them
  relevant. A name with no rationale is noise.
- **Prefer precision over coverage.** A tight, well-justified shortlist is more useful
  than an exhaustive one; the cost of a bloated list is that the people who matter get
  lost in it.
- **Don't fabricate people or attributes.** Only *rank* stakeholders that have an
  entry, and only cite remit/concerns/relationships that their entry actually states.
  People known only from `[[wiki-links]]` go in the "referenced but not in the wiki"
  note, unscored — never in the ranked list. If the issue clearly needs a role that no
  one in the repo holds, say so — that gap is useful information.
