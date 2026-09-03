# The Merge — Launch Atlas

A responsive, self-contained launch microsite built as one portable HTML file.

> **Demo boundary:** This is a fictional portfolio demo. Names, teams, launch events, resources, statuses and dates shown in the interface are illustrative—not claims about OpenAI or any real organization. The contact form is a client-side interaction demo; form inputs are not transmitted or persisted by the page code.

## Open on mobile

**[Launch the site](https://raw.githack.com/umutseve4/the-merge-launch/main/index.html)**

The preview is served by the third-party RawGitHack service, which may process ordinary request metadata when the page is opened. For an offline review, download `index.html` and open it locally.

## Project facts

- Entry point: `index.html`
- No build step or package manager
- No external runtime dependencies
- Responsive navigation and layouts
- Reduced-motion support and semantic labels

## Local use

Download `index.html` and open it in any modern browser.

## Verification

GitHub Actions parses the page with Python's standard library, rejects external runtime references and network/storage APIs, checks form behavior and baseline accessibility markers, and enforces the repository's governance files and demo boundary. Static validation does not establish full accessibility conformance or visual correctness.
