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

### 1. Understand the issue and the meeting, then ask a few check questions

Restate the issue in your own words so the user can correct you, then ask a **small**
number (usually 2–3) of short clarifying questions — and make them *grounded in what
the dataset actually distinguishes*, not generic project questions. The reason to
ask is that the same one-line issue ("data migration from AWS to Azure") can point at
very different people depending on details the user hasn't said yet: is regulated or
customer data in scope (pulls in compliance and data architecture), is it a one-off
or part of a standing transformation programme (pulls in the programme's people),
which domain's systems are moving (pulls in that domain's architect and tribe lead)?

**The single most important thing to establish is what kind of meeting this is**,
because it sets the *altitude* of everyone you should surface (see step 3). The same
topic needs a different room depending on whether it's a:

- **Design / working session** — making the technical decision and doing the work.
- **Tactical session** — planning, sequencing, committing teams, coordinating delivery.
- **Strategic / steering session** — setting direction, mandate, investment, sign-off.

If the user's wording already tells you ("technical design session", "set our
payments strategy", "plan next quarter"), infer it and say so. If it's genuinely
ambiguous, make the meeting type one of your check questions — it changes the answer
more than almost anything else.

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

As you read each entry, also note two things you'll need in step 3: the person's
**altitude** (are they hands-on, a discipline lead, or a senior leader?) and which
**stream** they sit in (their reporting/functional chain around a domain or
discipline). Both come from the Relationships section plus the role title — "Head
of", "Chief", "Director" and being the *functional leader* of several people signal
seniority; having no reports and a maker-style title signals hands-on.

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

### 3. Calibrate to the meeting: altitude and one voice per stream

A relevant person can still be the *wrong* person for this particular meeting. Two
adjustments turn a relevance list into the right room:

**Match altitude to the meeting type.** Bias the roster toward the level the meeting
operates at — relevance gets you onto the longlist, but altitude decides who actually
belongs:

- **Design / working session** → the people who'll make and live with the technical
  decision: domain/integration/cloud/data architects, engineers, delivery leads. A
  "Head of" or functional leader is usually *too senior* here — include one only if
  the design genuinely hinges on their expertise or sign-off. Inviting leadership to a
  working session slows it down without adding signal.
- **Tactical session** → the layer that turns direction into a plan and commits teams:
  domain architects, the head of a single discipline, tribe leads. Not every engineer,
  not the top strategy owner.
- **Strategic / steering session** → the senior leaders who set direction, hold the
  budget, and sign off: "Head of", "Chief", "Director", functional leaders, the
  escalation chain. Working-level specialists are usually *represented by their leader*
  rather than in the room — surface the leader, not the whole team.

So the same person can be a 9 for a design session and a 3 for a strategy session, or
vice versa. Let the meeting type move the scores, and say it did.

**One voice per stream.** Don't invite two adjacent levels of the *same reporting or
functional chain* — a lead architect and an architect under them, or a head and a
tribe lead in the same line. The Relationships section is how you spot it: if one
person sits in another's management/functional chain (directly or transitively) and
they'd speak to the *same* concern, they're one stream. Pick the single person at the
altitude the meeting calls for, and note whom they stand in for, rather than stacking
the chain. A senior in a strategy session already represents the team below; the
hands-on person in a design session is the one who matters, not their boss.

Be careful not to over-collapse: people in the same domain with **genuinely different
remits** (architecture vs delivery vs compliance) are *different* streams of concern
and may both belong — collapse only when one truly substitutes for the other on this
issue. When you drop someone for this reason, move them to a "represented by …" note
rather than deleting them silently, so the user can overrule you.

**The room-breadth toggle.** There's one case where reasonable people disagree: a
*same-line, different-remit* second voice — most often a tribe/delivery lead sitting
under the domain architect, in a strategy or steering room. Two defensible rooms:

- **Tight (leadership-only):** the single most senior person in the line represents
  everyone below them, *including* the different-remit reports. The domain architect
  carries the delivery line's view into the room; the tribe lead is "represented by".
  Right when the session is purely about direction, mandate, and money.
- **Inclusive (feasibility-aware):** keep the different-remit second voice in the room
  (ranked by altitude fit) because they bring something the leader can't fully stand
  in for — e.g. "can we actually build this, and what will it cost". Right when the
  session weighs deliverability or an investment case, not just direction.

Infer the default from the framing — a bare "set the strategy / steering session"
leans **tight**; any signal of "can we deliver this / what's the cost / investment
case" leans **inclusive**. If it's genuinely unclear and the choice changes the room,
make it one of your check questions ("tight leadership room, or should I keep a
delivery-feasibility voice?"). Either way, **state which mode you used** and keep the
collapsed person in the "represented by" note, so switching modes is a one-line ask.

### 4. Score, filter, and explain

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

Lead with a one-line read of the issue **and the meeting type you're sizing the room
for** (including any assumptions you made), then list the relevant stakeholders
**ordered by score, highest first**. For each:

```markdown
### <Name> — <Role> · relevance <N>/10
<1–3 sentences: why they're relevant, naming which axis drives it — remit
(they own/sign off), concern (it touches their stated lens), or structural
(programme / dotted-line / reporting chain). If the meeting type moved their score
(altitude too senior/junior for this room), say so. If a specific concern or remit
line from their entry applies, cite it. Optionally end with what to ask them or
align on.>
```

Then close with up to three short boundary notes, so the shortlist's edges are legible
and the user can catch a miss:

- **Deliberately left out** — profiled people you considered but didn't rank, and why
  (e.g. "Cloud Architect — relevant at build time, not for this decision"; or "too
  senior for a design session").
- **Represented by their stream** — where you collapsed a reporting chain to one
  voice, name who you dropped and who stands in for them (e.g. "Tribe Lead omitted —
  the Domain Architect represents the payments line for a strategy session"). This
  makes the one-voice-per-stream call reversible.
- **Referenced but not in the wiki** — important-looking people who appear only as
  `[[wiki-links]]` with no entry (managers, functional leaders, programme sponsors).
  Name them and say why they'd matter, but **do not score them** — flag that their
  entry is missing and that adding it would let you place them properly. This is
  where the escalation/sign-off chain usually surfaces (and it's often exactly the
  altitude a strategy session needs).

If your check questions went unanswered, state the assumptions the shortlist rests on
so the user can redirect you.

## Notes

- **Relevance needs a reason.** Never list a name without saying which axis makes them
  relevant. A name with no rationale is noise.
- **Prefer precision over coverage.** A tight, well-justified shortlist is more useful
  than an exhaustive one; the cost of a bloated list is that the people who matter get
  lost in it.
- **Right altitude, one voice per stream.** Let the meeting type set the level
  (design → makers, strategy → leaders) and don't stack two levels of the same
  reporting chain — pick the person who fits the room and note whom they represent.
- **Don't fabricate people or attributes.** Only *rank* stakeholders that have an
  entry, and only cite remit/concerns/relationships that their entry actually states.
  People known only from `[[wiki-links]]` go in the "referenced but not in the wiki"
  note, unscored — never in the ranked list. If the issue clearly needs a role that no
  one in the repo holds, say so — that gap is useful information.
