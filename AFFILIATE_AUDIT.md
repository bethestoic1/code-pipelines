# Affiliate audit — codepipelines.com (Apex Affiliate Oracle)

**Date:** 2026-03-04  
**Scope:** All affiliate links, placement, and conversion design across the repo.

---

## 1. Validity & accuracy ✅

| Program | Live URL | Where used | Status |
|--------|----------|------------|--------|
| **BrainGrid** | `https://braingrid.link/stoic` | Homepage footer, blog index footer, all 28 blog articles (CTA box + inline + footer) | ✅ Valid, consistent |
| **Replit** | `https://replit.com/refer/bethestoic1` | replit-ai-vs-cursor (body + CTA), deploy-ai-apps (body), lovable-vs-cursor (body) | ✅ Valid, correct placement |
| **Vultr** | `https://www.vultr.com/?ref=9876695-9J` (promo) | deploy-ai-apps, best-hosting-for-developers (inline + “Try Vultr”) | ✅ Valid; promo link; switch to `ref=9876694` when promo ends |
| **Udemy** | `https://refer.udemy.com/bethestoic1!bf999b8a03!a?locale=en` | Generator only (`UDEMY_REFERRAL_URL`); no learning-path articles live yet | ✅ Ready for Tier 3 add-ons #32–33 when created |

**Generator (`scripts/generate_articles.py`):**  
- `REPLIT_REFERRAL_URL`, `UDEMY_REFERRAL_URL`, `VULTR_REFERRAL_URL` match BRAINGRID_AFFILIATE.md.  
- CTA template uses `https://braingrid.link/stoic` correctly.  
- New articles get BrainGrid CTA only; Replit/Vultr CTAs are added manually in deploy/replit/hosting articles (documented in BRAINGRID_AFFILIATE.md).

**Doc vs site:**  
- BRAINGRID_AFFILIATE.md says “All 28 blog articles” — count is correct (28 posts, each with CTA + footer).  
- No broken or mismatched affiliate URLs found.

---

## 2. Gaps and risks

| Issue | Severity | Recommendation |
|-------|----------|----------------|
| **Homepage** has no above-the-fold affiliate CTA | Medium | Only footer links to BrainGrid. Add a visible “Try BrainGrid →” (or “Ship faster with BrainGrid”) in header or hero so high-intent visitors see it without scrolling. |
| **Blog index** has no CTA before the list | Low | Add one line before the post list: “We recommend BrainGrid for Cursor/Claude Code users. [Try BrainGrid →]” to capture blog-only visitors. |
| **External links** lack `rel="noopener"` | Low | Add `rel="noopener noreferrer"` to all external affiliate links (security best practice). Optionally `rel="sponsored"` for disclosure where required. |
| **Udemy** not used in any article yet | Info | No error. Use `UDEMY_REFERRAL_URL` when you publish learning-path / course articles (CONTENT_PLAN #32–33). |
| **DigitalOcean** not live | Expected | BRAINGRID_AFFILIATE.md says get DO approval and add to deploy/hosting content; no link until approved. |

---

## 3. Placement design — highest probable clicks & purchases

**Current strengths**

- **BrainGrid:** In every post (CTA box + footer), plus inline where context fits (e.g. “add BrainGrid to your stack”). CTA copy is consistent and benefit-led (“Ship faster with your stack”).  
- **Replit:** First body mention + dedicated CTA line in Replit vs Cursor (“Try Replit → (you and a friend get $10 in credits)”). Clear value prop.  
- **Vultr:** Inline in deploy and hosting posts with “Try Vultr (referral link—new users get credits).” Fits intent.  
- **Tier 1 comparison posts** (Cursor vs Copilot, Best AI coding assistant, Cursor pricing) have multiple BrainGrid mentions + CTA — good for high-intent traffic.

**Improvements for conversion**

1. **Homepage:** Add one primary affiliate CTA next to or below “Compare AI coding tools 2026” (e.g. “Try BrainGrid for Cursor/Claude Code →”). Keeps compare as main action but surfaces the recurring-revenue link above the fold.  
2. **Blog index:** One-line CTA before the list so visitors who land on /blog/ see the recommendation immediately.  
3. **Long articles:** Consider a second CTA block after the first or second section on 1,500+ word posts to capture early leavers.  
4. **CTA order in CTA box:** On Replit article, Replit CTA is first (contextual), then BrainGrid. On others, “Compare more tools” then “Ship faster… BrainGrid.” Keeping BrainGrid last as the main “try this” is fine; ensure the link is the most prominent (e.g. “Try BrainGrid →” as button-style or bold).  
5. **rel attribute:** Add `rel="noopener noreferrer"` to all external affiliate links sitewide; add `rel="sponsored"` if any program or jurisdiction requires affiliate disclosure in markup.

---

## 4. Pain points → Trends → Top affiliate plays (recap)

| Pain point | 2026 trend | Affiliate play on site |
|------------|------------|------------------------|
| “Which AI coding tool?” | Agentic adoption, credit-based pricing | BrainGrid in all comparison posts ✅ |
| “Vibe coding” vs integrity | Diff-based workflows, specs | BrainGrid (planning/spec layer) ✅ |
| Credit/pricing confusion | Cursor credits, Copilot seats | Cursor pricing post + BrainGrid as complement ✅ |
| Onboarding / time-to-first-commit | Context, MCP, docs | BrainGrid in onboarding post ✅ |
| Multi-agent vs single-agent | Orchestration narrative | BrainGrid in agentic/multi-agent posts ✅ |
| Deploy/hosting | VPS, managed, serverless | Vultr ✅; DigitalOcean when approved |
| Learning / browser IDE | Replit, quick prototypes | Replit referral ✅ |

---

## 5. Monetization strategy (audit alignment)

- **Traffic first:** Tier 1–2 bodies expanded → more rankings and sessions; CTAs already in place.  
- **BrainGrid live sitewide:** No missing pages; focus on quality and internal links.  
- **Deploy/hosting:** Vultr live in deploy + best-hosting; DO to be added when approved.  
- **Replit/Udemy:** Replit used where relevant; Udemy ready for future learning-path content.

---

## 6. Passive income projection (unchanged)

- **BrainGrid:** ~10 referrals/mo at ~$20/mo × 15% ≈ **$30/mo**; scales with traffic.  
- **12‑month goal:** 500–2K organic sessions/mo → 20–50 referrals/mo → **$100–400/mo** recurring with consistent content and CTAs.

---

## 7. Single next step (post-audit)

1. **Done in this audit:** Add prominent BrainGrid CTA on homepage and one-line CTA on blog index; add `rel="noopener noreferrer"` in generator for new articles.  
2. **Applied (full pass):** All existing blog HTML updated with `rel="noopener noreferrer"` on every `braingrid.link`, `replit.com/refer`, and `vultr.com/?ref` link. Cursor vs Copilot 2026 and Best AI coding assistant 2026 expanded to 1,500+ words with extra comparison content, Security/compliance section (Cursor vs Copilot), mid-article CTAs, and internal links to cursor-pricing, agentic-workflows, tabnine-vs-cursor, windsurf-vs-cursor, claude-code-vs-cursor-agent, replit-ai-vs-cursor, and related posts.

---

**Summary:** All affiliate links are **valid and accurate** and match BRAINGRID_AFFILIATE.md and the generator. The repo is **designed for recurring referrals** with BrainGrid primary and Replit/Vultr in context. The changes above are aimed at **highest probable clicks and purchases** by surfacing the main affiliate CTA on the homepage and blog index and tightening link hygiene for new and existing pages.
