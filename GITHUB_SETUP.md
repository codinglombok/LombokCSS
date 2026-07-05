# Publishing LombokCSS to GitHub — maintainer guide

A detailed, open-source-standard walkthrough: from an empty GitHub account to a
live repo with CI, hosted docs, automated changelog/releases, and npm + CDN
distribution. Commands assume the org/user **`codinglombok`** and repo
**`lombokcss`** (already set throughout the project).

> TL;DR of the automated flow once set up:
> **commit (Conventional Commits) → push → release-please opens a "release PR" →
> you merge it → it tags + creates a GitHub Release and publishes to npm →
> jsDelivr/unpkg serve it; Pages redeploys the docs.**

---

## 0. Prerequisites

| Tool | Why | Check |
|------|-----|-------|
| Git | version control | `git --version` |
| GitHub account | hosting | — |
| GitHub CLI (`gh`) | optional, easiest repo creation | `gh --version` |
| Node.js ≥ 18 | build + publish | `node -v` |
| npm account | npm publishing (optional) | `npm whoami` |
| Docker | refresh visual baselines to match CI (optional) | `docker --version` |

One-time identity config (if you've never set it):

```bash
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"
```

---

## 1. Final prep before first push

1. **Placeholders.** Org URLs already say `codinglombok`. Still replace the two
   email placeholders if you want real contacts:
   - `your-domain.example` in `SECURITY.md` and `CODE_OF_CONDUCT.md`.
2. **Confirm the package name is free on npm** (skip if you won't publish to npm):
   ```bash
   npm view lombokcss        # "404 Not Found" = available
   ```
   If it's taken, switch to a scoped name in `package.json`:
   `"name": "@codinglombok/lombokcss"` (the workflows already use
   `--access public`, which scoped packages require).
3. **Sanity build locally:**
   ```bash
   npm install
   npm run build
   npm run size:check
   ```

---

## 2. Initialize git & make the first commit

The repo uses **Conventional Commits** so release-please can derive versions and
changelogs. Use that style from commit #1.

```bash
cd lombokcss
git init -b main
git add .
git commit -m "feat: initial LombokCSS release"
```

Conventional Commit prefixes you'll use most: `feat:` (minor bump),
`fix:` (patch), `docs:`, `refactor:`, `chore:`, `test:`, `ci:`. A `feat!:` or a
`BREAKING CHANGE:` footer triggers a major bump.

---

## 3. Create the GitHub repo and push

**Option A — GitHub CLI (recommended):**
```bash
gh auth login                     # once
gh repo create codinglombok/lombokcss \
  --public --source=. --remote=origin --push \
  --description "Token-first component CSS framework. One markup, five styles, dark + RTL."
```

**Option B — web UI:**
1. github.com → **New repository** → owner `codinglombok`, name `lombokcss`,
   **Public**, do **not** add README/license (the project already has them).
2. Connect & push:
   ```bash
   git remote add origin https://github.com/codinglombok/lombokcss.git
   git push -u origin main
   ```
   For HTTPS, the "password" prompt wants a **Personal Access Token** (classic,
   scope `repo`), not your account password.

After pushing, the **CI** and **Visual regression** workflows run on the
**Actions** tab.

---

## 4. Configure the repository (open-source standard)

Repo → **Settings**:

### About / discoverability
- Add a **Description** and **Website** (your Pages URL, step 6).
- Add **Topics**: `css`, `framework`, `design-system`, `design-tokens`,
  `components`, `dark-mode`, `rtl`, `glassmorphism`, `neo-brutalism`.
- Upload a **Social preview** image (Settings → General) for nice link cards.

### Actions permissions (required for automation)
Settings → **Actions → General**:
- **Workflow permissions:** "Read and write permissions".
- Tick **"Allow GitHub Actions to create and approve pull requests"**
  (release-please opens its release PR with this).

### Branch protection (Settings → Branches → Add rule, branch `main`)
- ✅ Require a pull request before merging.
- ✅ Require status checks to pass → select **CI** and **Visual regression**.
- ✅ Require branches to be up to date before merging.
- ✅ Require linear history (optional, keeps tidy tags).
- Keep it light if you're solo; you can still allow yourself to merge.

### Features
- Enable **Issues** and **Discussions** (the issue template config links to
  Discussions). Disable **Wiki/Projects** if unused.

---

## 5. npm publishing setup (optional but recommended)

1. Create an npm account, enable **2FA**.
2. Create an **automation** access token:
   npmjs.com → avatar → **Access Tokens → Generate New Token → Automation**.
3. Add it to GitHub: repo → **Settings → Secrets and variables → Actions →
   New repository secret** → name **exactly** `NPM_TOKEN` → paste the token.

That's all the automated flow needs. **Provenance** (the verified "Built and
signed on GitHub Actions" badge on npm) works automatically because the publish
runs in Actions on a public repo with `id-token: write`.

---

## 6. Enable GitHub Pages (hosted docs)

Settings → **Pages** → **Source: GitHub Actions**. (One-time; the workflow can't
turn Pages on itself.) On the next push to `main`, `pages.yml` rebuilds the docs
and deploys them to:

```
https://codinglombok.github.io/lombokcss/
```

Put that URL in the repo **Website** field and the README.

---

## 7. Cut your first release

You generally **don't** run `npm version` by hand — release-please does it.

1. Land commits on `main` (directly or via PRs) using Conventional Commits.
2. release-please opens a PR titled like **"chore(main): release 0.1.0"** that
   updates `CHANGELOG.md` and `package.json`.
3. Review and **merge** that PR. release-please then:
   - creates the git **tag** `v0.1.x` and a **GitHub Release**, and
   - runs the gated **npm publish** step (with provenance) in the same workflow.
4. Within minutes, the package is on npm and the CDNs serve it.

Manual fallback (rarely needed): Actions → **Publish to npm (manual fallback)** →
**Run workflow**.

---

## 8. Verify everything

- **CI:** green check on the latest commit (build + size budget + stale-dist
  guard + visual tests).
- **Docs:** `https://codinglombok.github.io/lombokcss/` loads; style/dark/RTL
  switchers work and persist across pages.
- **npm:** `https://www.npmjs.com/package/lombokcss` shows the version and a
  provenance statement.
- **CDN:**
  ```
  https://cdn.jsdelivr.net/npm/lombokcss@0.1.0/dist/lombok.min.css
  https://unpkg.com/lombokcss@0.1.0/dist/lombok.min.css
  ```
  (For a scoped name: `.../npm/@codinglombok/lombokcss@0.1.0/dist/lombok.min.css`.)
- **Badges** in the README go live automatically once the repo/package exist.

---

## 9. Day-to-day maintenance

- **Edit `src/`, never `dist/`.** After changes: `npm run build` and commit the
  updated `dist/` (CI fails if it's stale). Update docs with `npm run build:docs`.
- **Dependabot** opens weekly PRs for npm + Actions updates; merge the green ones.
- **Visual changes are intentional?** Refresh baselines **in the pinned
  Playwright image** so they match CI exactly:
  ```bash
  docker run --rm -v "$PWD":/work -w /work mcr.microsoft.com/playwright:v1.56.0-noble \
    bash -c "npm ci && npm run build && npm run build:docs && npm run test:visual:update"
  ```
  Commit the updated PNGs under `tests/visual.spec.js-snapshots/`.
- **Formatting:** `npm run format` before committing.

---

## 10. Troubleshooting (common open-source gotchas)

| Symptom | Cause / fix |
|---------|-------------|
| release-please never opens a PR | Enable "Allow GitHub Actions to create and approve pull requests" + read/write workflow permissions (step 4). Also: commits must be Conventional Commits. |
| Release created but nothing published | Ensure `NPM_TOKEN` secret exists and the publish steps in `release-please.yml` are gated on `release_created` (they are). |
| `npm publish` 402 / 403 | For a scoped name you need `--access public` (set). For 403, the name may be taken or the token lacks publish rights. |
| Provenance fails | Repo must be **public**, publish must run **in Actions**, job needs `id-token: write` (set). |
| CI fails on "dist is out of date" | Run `npm run build` and commit `dist/`. |
| Pages 404 | Set **Settings → Pages → Source: GitHub Actions** once. |
| Visual tests fail after a browser bump | Bump the container tag in `visual.yml` **and** the `@playwright/test` version together, then regenerate baselines in that image. |

---

## 11. Distributing via other registries

- **Composer / Packagist:** `composer.json` is included. Submit the repo at
  packagist.org → **Submit**, then enable the GitHub hook so new tags publish
  automatically. Users install with `composer require codinglombok/lombokcss`.
- **CDN:** no action needed beyond an npm release — jsDelivr and unpkg mirror npm.

---

That's the full path from zero to a properly governed, automatically released
open-source project. Once steps 4–6 are done once, the recurring loop is just:
commit → merge the release PR → done.
