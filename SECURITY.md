# Security Policy

## Supported versions

LombokCSS is a CSS/JS asset package. Security fixes land on the latest release.

| Version | Supported |
| ------- | --------- |
| 0.1.x   | ✅        |
| < 0.1   | ❌        |

## Reporting a vulnerability

Please **do not** open a public issue for security reports.

- Preferred: open a private report via GitHub
  **Security → Advisories → "Report a vulnerability"** on this repository.
- Or email **security@your-domain.example**.

Include: a description, affected version(s), reproduction steps, and impact.

We aim to acknowledge within 72 hours and to ship a fix or mitigation as soon
as is practical, crediting reporters who wish to be credited.

## Scope notes

The optional `lombok.js` only attaches DOM event listeners and exposes a small
`Lombok.toast()` helper; it makes no network requests and uses no storage.
The CSS uses `backdrop-filter`, `:has()`, and logical properties with
fallbacks. Report anything that could enable CSS injection, clickjacking via
overlay components (modal/drawer), or focus-trap escapes.
