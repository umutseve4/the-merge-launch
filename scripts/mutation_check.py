#!/usr/bin/env python3
"""Break the site on purpose and require the gate to notice.

A passing gate is evidence only if it is capable of failing. This copies the
repository into a scratch directory, applies one targeted mutation at a time,
and requires scripts/validate_site.py to exit non-zero for each. A mutation
that does not change any file is treated as a broken test, not as a pass, so
this file cannot rot into a no-op while still reporting green.
"""

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
VALIDATOR = REPO / "scripts" / "validate_site.py"
COPIED = ["index.html", "README.md", "CONTRIBUTING.md", "SECURITY.md", ".gitignore"]


def replace(path, old, new):
    def apply(root):
        target = root / path
        text = target.read_text(encoding="utf-8")
        assert old in text, f"mutation anchor not found in {path}: {old!r}"
        target.write_text(text.replace(old, new, 1), encoding="utf-8")
    return apply


def inject(snippet):
    def apply(root):
        target = root / "index.html"
        text = target.read_text(encoding="utf-8")
        assert "</body>" in text, "index.html has no </body> to inject before"
        target.write_text(text.replace("</body>", snippet + "</body>", 1), encoding="utf-8")
    return apply


def delete(path):
    def apply(root):
        (root / path).unlink()
    return apply


# Each mutation names the condition it is meant to trip.
MUTATIONS = [
    ("required files: SECURITY.md removed", delete("SECURITY.md")),
    ("page title changed", replace("index.html", "<title>", "<title>Something Else</title><!--")),
    ("external reference added", inject('<img src="https://example.com/pixel.png" alt="">')),
    ("script src added", inject('<script src="app.js"></script>')),
    ("stylesheet link added", inject('<link rel="stylesheet" href="theme.css">')),
    ("iframe added", inject('<iframe src="local.html" title="x"></iframe>')),
    ("form given a submission target", replace("index.html", "<form", "<form action=\"/subscribe\"")),
    ("browser storage used", inject("<script>const seen = localStorage;</script>")),
    ("document language removed", replace("index.html", "<html lang=\"en\">", "<html>")),
    ("navigation landmark label removed", replace("index.html", "aria-label=\"Main navigation\"", "data-was=\"nav\"")),
    ("disclosure state removed", replace("index.html", "aria-expanded=\"false\"", "data-was=\"expanded\"")),
    ("live region removed", replace("index.html", "aria-live=\"polite\"", "data-was=\"live\"")),
    ("unlabelled control added", inject('<input id="orphan-control" type="text">')),
    ("reduced-motion support removed", replace("index.html", "@media(prefers-reduced-motion:reduce)", "@media(min-width:1px)")),
    ("README demo disclosure removed", replace("README.md", "fictional portfolio demo", "production system")),
    ("README form disclosure removed", replace("README.md", "form inputs are not transmitted or persisted by the page code", "the form works")),
]


def run_validator(root):
    return subprocess.run([sys.executable, str(VALIDATOR)], cwd=root, capture_output=True, text=True)


def copy_repo(root):
    for name in COPIED:
        shutil.copy2(REPO / name, root / name)


failures = []

with tempfile.TemporaryDirectory() as tmp:
    control = Path(tmp) / "control"
    control.mkdir()
    copy_repo(control)
    baseline = run_validator(control)
    if baseline.returncode != 0:
        print("FAIL: the unmutated copy does not pass, so no mutation result would mean anything.")
        print(baseline.stdout + baseline.stderr)
        sys.exit(1)
    print("control: unmutated copy passes")

for index, (name, mutate) in enumerate(MUTATIONS, start=1):
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "case"
        root.mkdir()
        copy_repo(root)
        before = sorted((p.name, p.read_bytes()) for p in root.iterdir())
        mutate(root)
        after = sorted((p.name, p.read_bytes()) for p in root.iterdir())
        if before == after:
            failures.append(f"{name}: the mutation changed nothing, so it proves nothing")
            print(f"BROKEN   {index:2d}. {name}")
            continue
        result = run_validator(root)
        if result.returncode == 0:
            failures.append(f"{name}: the gate stayed green")
            print(f"SURVIVED {index:2d}. {name}")
        else:
            print(f"caught   {index:2d}. {name}")

print()
if failures:
    print(f"FAIL: {len(failures)} of {len(MUTATIONS)} mutations were not caught:")
    for failure in failures:
        print(f"  - {failure}")
    sys.exit(1)

print(f"PASS: all {len(MUTATIONS)} mutations were caught by the gate.")
