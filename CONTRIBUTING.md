# Contributing

## Workflow

1. Create a focused branch from the current `main` branch.
2. Keep each pull request limited to one auditable concern.
3. Do not add a build system or runtime dependency without a demonstrated need.
4. Preserve the fictional-demo and client-only form disclosure in `README.md`.
5. Do not present illustrative people, organizations, resources, dates or system statuses as real.

## Verification

Open a pull request and require the `Static QA` workflow to pass. The check parses `index.html`, rejects external runtime references, verifies repository governance files and enforces the demo boundary.

For visual changes, also inspect the page in a modern desktop and mobile browser. Automated static validation does not prove visual correctness, browser compatibility or accessibility conformance.
