# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Static affiliate/content site targeting AI developer tool audiences (Cursor, Claude Code, GitHub Copilot, Windsurf, etc.). Hosted on GitHub Pages at `codepipelines.com`. No build framework — pure HTML/CSS with a Python content generation script.

## Commands

**Generate article stubs:**
```bash
python3 scripts/generate_articles.py
```
Reads the `ARTICLES` list in the script and writes HTML files to `/blog/`. Only run this to add new article stubs; expanding article content is done by editing the generated HTML directly.

**No other build, lint, or test commands exist.** The site deploys automatically via GitHub Pages on push to `main`.

### Git workflow

**Always pull from `main` first** before committing (or before starting new work). This avoids branch divergence when `main` has moved forward (e.g. merged PRs). Example: `git fetch origin && git pull origin main --no-rebase` (or merge/rebase as preferred), then make and commit changes.

## Architecture

### File structure

- `index.html` — Homepage
- `blog/index.html` — Blog listing
- `blog/*.html` — 28+ article pages (some generated, some manually expanded)
- `scripts/generate_articles.py` — Generates article stubs with shared nav/footer/CTA/schema
- `sitemap.txt` — Must be updated manually when new articles are added
- `CONTENT_PLAN.md` — Master list of all planned articles (Tier 1–6), target queries, and affiliate assignments
- `PROGRESS.md` — Task checklist for resuming work across sessions
- `BRAINGRID_AFFILIATE.md` — Affiliate link strategy and all referral URLs

### HTML page conventions

Every page (homepage, blog index, articles) follows this structure:
- Embedded CSS only (no external stylesheets)
- CSS custom properties: `--bg: #0d0d0d`, `--accent: #33ff33`, `--space: 8px`, `--font` (monospace)
- Dark terminal aesthetic; `max-width: 720px` for articles, `900px` for homepage
- Accessibility: `.skip-link` → `#main`, semantic `<header>/<nav>/<main>/<footer>`, `aria-label` on nav
- `@media (prefers-reduced-motion)` on animations
- SEO: `<link rel="canonical">`, Open Graph tags, Twitter Card, JSON-LD `Article` schema
- Affiliate links: always use `rel="noopener noreferrer"`

### Article page structure

```
skip-link → header/nav → main#main → article
  h1 (title)
  p.meta (date · Code Pipelines)
  intro paragraph
  h2 sections with content
  p.related (2–3 internal links before CTA)
  div.cta-box (affiliate CTAs)
footer
script[type="application/ld+json"] (Article schema)
```

### Content strategy

Articles are organized in tiers by conversion priority (see `CONTENT_PLAN.md`):
- **Tier 1** (highest): AI tool comparisons (Cursor vs Copilot, best AI assistant, pricing)
- **Tier 2**: Agentic/workflow authority content
- **Tier 3**: Productivity how-tos and onboarding
- **Tiers 4–6**: Security, hosting/infra, MCP/plugins

### Affiliate links

Referral URLs are defined as constants in `scripts/generate_articles.py`:
- `BRAINGRID_REFERRAL_URL` — Primary affiliate; appears in every article CTA box and footer
- `REPLIT_REFERRAL_URL` — Use in deploy/learning articles
- `VULTR_REFERRAL_URL` — Use in hosting/deploy articles

### Adding a new article

1. Add the article metadata to `ARTICLES` list in `scripts/generate_articles.py`
2. Run `python3 scripts/generate_articles.py` to generate the stub
3. Expand content in `blog/<slug>.html` (target 1,500–2,500 words for comparisons, 1,000+ for how-tos)
4. Add 2–3 internal `p.related` links before the CTA box
5. Add the URL to `sitemap.txt`
6. Reference the article from `blog/index.html` and relevant existing articles
