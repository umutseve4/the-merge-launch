<h1 align="center">The Merge: Launch Atlas</h1>

<p align="center">
  A full launch microsite that lives in one HTML file.<br>
  Responsive navigation, sectioned launch atlas, reduced-motion support,<br>
  no build step, no package manager, no external runtime dependency.
</p>

<p align="center">
  <a href="https://github.com/umutseve4/the-merge-launch/actions/workflows/static-qa.yml"><img src="https://github.com/umutseve4/the-merge-launch/actions/workflows/static-qa.yml/badge.svg" alt="Static QA"></a>
  <a href="https://github.com/umutseve4/the-merge-launch/actions/workflows/pages.yml"><img src="https://github.com/umutseve4/the-merge-launch/actions/workflows/pages.yml/badge.svg" alt="Pages"></a>
  <img src="https://img.shields.io/badge/source%20files-1%20HTML-FF4D4F?style=flat-square" alt="1 HTML file">
  <img src="https://img.shields.io/badge/runtime%20dependencies-0-FF4D4F?style=flat-square" alt="0 dependencies">
</p>

<p align="center">
  <b><a href="https://umutseve4.github.io/the-merge-launch/">Open the live site</a></b>
</p>

---

## 30 seconds

Click the link above. It works on mobile, and it is served from this
repository's own GitHub Pages deployment, so the bytes you receive are the
bytes CI validated. You can also download `index.html` and double-click it;
there is nothing else to install and the page works offline.

## Project facts

| | |
|---|---|
| Live site | https://umutseve4.github.io/the-merge-launch/ |
| Entry point | `index.html` |
| Build step | none |
| Package manager | none |
| External runtime dependencies | none |
| Accessibility | reduced-motion support, semantic labels |
| Layout | responsive navigation and sections |

## Verification

`scripts/validate_site.py` is the single quality gate. GitHub Actions runs it
twice: once on every push and pull request, and once again inside the publish
workflow before anything is deployed. It parses the page with Python's standard
library, rejects external runtime references and network/storage APIs, checks
form behavior and baseline accessibility markers, and enforces the repository's
governance files and demo boundary. If the gate fails, nothing is published.

## Limits

- **This is a fictional portfolio demo.** Names, teams, launch events, resources, statuses and dates shown in the interface are illustrative, not claims about OpenAI or any real organization.
- The contact form is a client-side interaction demo; form inputs are not transmitted or persisted by the page code.
- Static validation does not establish full accessibility conformance or visual correctness; both need a separate manual pass.
