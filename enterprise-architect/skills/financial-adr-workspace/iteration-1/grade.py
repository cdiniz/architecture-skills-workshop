#!/usr/bin/env python3
import json, re, os, glob

BASE = os.path.dirname(os.path.abspath(__file__))

def load(eval_dir, cfg):
    files = glob.glob(os.path.join(BASE, eval_dir, cfg, "outputs", "**", "*.md"), recursive=True)
    if not files:
        return None, None
    p = files[0]
    return p, open(p).read()

def has(text, *patterns):
    return any(re.search(p, text, re.I) for p in patterns)

MARKER = r"\[(OPEN QUESTION|DECISION PENDING|ASSUMPTION|NEEDS COMPLIANCE|CLARIFICATION)"

def grade_eval0(path, t):
    fname = os.path.basename(path)
    return [
        ("ADR file created under docs/adr with zero-padded number", bool(re.match(r"\d{3,4}-", fname)) and "/docs/adr/" in path),
        ("Identifies PCI DSS as applicable regime", has(t, r"PCI[\s-]?DSS")),
        ("States data classification of cardholder data / PAN", has(t, r"cardholder data", r"data classif", r"\bPAN\b")),
        ("Assesses third-party / vendor risk for the vault", has(t, r"third[\s-]?party", r"vendor", r"concentration") and has(t, r"risk|lock-?in|depend")),
        ("Security section on token/key handling or PCI scope reduction", has(t, r"key management", r"reduc\w+ .{0,20}scope", r"out of scope", r"token") ),
        ("Includes approvals / sign-off section", has(t, r"## Approval", r"sign[\s-]?off")),
        ("Does not fabricate approvers/owners — unknowns marked", has(t, MARKER)),
    ]

def grade_eval1(path, t):
    fname = os.path.basename(path)
    return [
        ("ADR file created under docs/adr with zero-padded number", bool(re.match(r"\d{3,4}-", fname)) and "/docs/adr/" in path),
        ("Documents options incl. on-prem and multi-cloud", has(t, r"on[\s-]?prem") and has(t, r"multi[\s-]?cloud")),
        ("Addresses data residency/sovereignty with EU regions", has(t, r"residen|sovereign") and has(t, r"eu-west-1|eu-central-1|EU\b|Ireland|Frankfurt")),
        ("Addresses resilience / DR (RTO/RPO/failover)", has(t, r"RTO|RPO|disaster recovery|failover|resilien")),
        ("Notes cloud concentration / third-party risk", has(t, r"concentration") or (has(t, r"single[\s-]?(cloud|provider|vendor)") and has(t, r"risk"))),
        ("Approvals section names architecture review board", has(t, r"architecture review board|\bARB\b")),
        ("Does not fabricate — gaps marked", has(t, MARKER)),
    ]

def grade_eval2(path, t):
    return [
        ("ADR file created", path is not None),
        ("Captures technical decision: event-driven / Kafka vs REST", has(t, r"event[\s-]?driven|Kafka") and has(t, r"REST|synchronous")),
        ("Surfaces PSD2 / Open Banking regulatory dimension", has(t, r"PSD2|Open Banking")),
        ("Uses uncertainty markers for unspecified regulated dims", has(t, MARKER)),
        ("Includes risk, security, and resilience considerations", has(t, r"risk") and has(t, r"security") and has(t, r"resilien|RTO|RPO|availab")),
        ("Does not assert unprovided compliance conclusions/approvers", has(t, MARKER)),
    ]

GRADERS = {
    "eval-0-pci-tokenisation": grade_eval0,
    "eval-1-data-residency": grade_eval1,
    "eval-2-kafka-openbanking": grade_eval2,
}

for eval_dir, grader in GRADERS.items():
    for cfg in ("with_skill", "without_skill"):
        path, text = load(eval_dir, cfg)
        if text is None:
            print(f"MISSING: {eval_dir}/{cfg}")
            continue
        results = grader(path, text)
        expectations = [{"text": name, "passed": bool(ok), "evidence": ("matched" if ok else "not found in output")} for name, ok in results]
        passed = sum(1 for _, ok in results if ok)
        total = len(results)
        out = {
            "expectations": expectations,
            "summary": {"passed": passed, "failed": total - passed, "total": total,
                        "pass_rate": round(passed / total, 4)},
        }
        run_dir = os.path.join(BASE, eval_dir, cfg, "run-1")
        os.makedirs(run_dir, exist_ok=True)
        json.dump(out, open(os.path.join(run_dir, "grading.json"), "w"), indent=2)
        # move timing into run-1 if present at config level
        src_t = os.path.join(BASE, eval_dir, cfg, "timing.json")
        if os.path.exists(src_t):
            dst_t = os.path.join(run_dir, "timing.json")
            os.replace(src_t, dst_t)
        print(f"{eval_dir}/{cfg}: {passed}/{total}")
