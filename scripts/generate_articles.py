#!/usr/bin/env python3
"""Generate blog article HTML files from CONTENT_PLAN. Run from repo root."""

import os
import re

BASE = "https://codepipelines.com/blog"
BLOG_DIR = os.path.join(os.path.dirname(__file__), "..", "blog")
DATE = "2026-03-02"

STYLES = """        :root {
            --bg: #0d0d0d;
            --surface: #1a1a1a;
            --text: #e0e0e0;
            --accent: #33ff33;
            --accent-muted: #2acc2a;
            --muted: #888;
            --space: 8px;
            --radius: 4px;
        }
        *, *::before, *::after { box-sizing: border-box; }
        .skip-link {
            position: absolute;
            top: -100%;
            left: var(--space);
            padding: 12px 16px;
            background: var(--accent);
            color: #000;
            font-weight: bold;
            text-decoration: none;
            z-index: 100;
            border-radius: var(--radius);
            min-height: 44px;
            display: inline-flex;
            align-items: center;
        }
        .skip-link:focus { top: var(--space); }
        body {
            font-family: 'Courier New', Courier, monospace;
            font-size: clamp(1rem, 2vw + 0.9rem, 1.125rem);
            line-height: 1.6;
            color: var(--text);
            background: var(--bg);
            max-width: 720px;
            margin: 0 auto;
            padding: 20px;
            position: relative;
        }
        header { border-bottom: 1px solid var(--accent); padding: 24px 0; }
        nav { margin-top: calc(var(--space) * 2); }
        nav a {
            color: var(--accent);
            text-decoration: none;
            margin-right: calc(var(--space) * 3);
            min-height: 44px;
            display: inline-flex;
            align-items: center;
        }
        nav a:hover { color: var(--accent-muted); }
        main { padding: calc(var(--space) * 4) 0; }
        article h1 { color: #fff; text-transform: uppercase; font-size: 1.25rem; }
        article h2 { color: #fff; font-size: 1.1rem; margin-top: calc(var(--space) * 5); }
        .meta { color: var(--muted); font-size: 0.9em; margin-bottom: calc(var(--space) * 4); }
        .cta-box {
            border: 1px solid var(--accent);
            padding: calc(var(--space) * 4);
            margin: calc(var(--space) * 5) 0;
            border-radius: var(--radius);
        }
        .cta-box a { color: var(--accent); font-weight: bold; }
        .cta-box a:hover { color: var(--accent-muted); }
        footer {
            margin-top: calc(var(--space) * 8);
            padding-top: calc(var(--space) * 3);
            border-top: 1px solid var(--muted);
            color: var(--muted);
            font-size: 0.9em;
        }
        footer a { color: var(--accent); }"""

NAV = """        <nav aria-label="Main">
            <a href="/">Home</a>
            <a href="/blog/">Blog</a>
            <a href="/blog/cursor-vs-copilot-2026.html">Compare AI coding tools 2026</a>
        </nav>"""

CTA = """            <div class="cta-box" aria-label="Compare tools">
                <p><strong>Compare more tools:</strong> <a href="/blog/">See our full DevEx and AI coding tool comparisons</a>.</p>
                <p><strong>Ship faster with your stack:</strong> We recommend <a href="https://www.braingrid.ai/">BrainGrid</a> for Cursor and Claude Code users. <a href="https://www.braingrid.ai/">Try BrainGrid →</a></p>
            </div>"""

def slugify(title):
    s = title.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-") + ".html"

ARTICLES = [
    ("Best AI coding assistant 2026 (Cursor, Claude Code, Windsurf, Tabnine)", "best-ai-coding-assistant-2026",
     "Compare the best AI coding assistants in 2026: Cursor, Claude Code, Windsurf, Tabnine, and more. Pricing, agentic features, and which fits your stack.",
     "We compare Cursor, Claude Code CLI, Windsurf, Tabnine, and other leading AI coding tools so you can choose the right assistant for 2026. This roundup covers pricing, agentic vs inline workflows, and who each tool is best for.",
     ["What to look for in 2026", "Quick comparison", "Our picks by use case"]),
    ("Cursor pricing 2026: credits, plans, and hidden costs", "cursor-pricing-2026",
     "Cursor pricing in 2026: how credits work, plan tiers, and what costs to watch. Plus how to get more value from your AI dev stack.",
     "Cursor moved to a credit-based model. Here’s how pricing works in 2026, what to expect at each tier, and how to avoid surprise costs while still shipping with agentic workflows.",
     ["How Cursor credits work", "Plan tiers and rough costs", "Getting more value from your stack"]),
    ("Claude Code CLI vs Cursor Agent: hands-on comparison", "claude-code-vs-cursor-agent-2026",
     "Claude Code CLI vs Cursor Agent in 2026: when to use which, pricing, and how they fit into an agentic dev workflow.",
     "Both support agentic, multi-step coding. We compare Claude Code CLI and Cursor Agent so you can choose—or use both—for your 2026 stack.",
     ["Claude Code CLI: strengths and workflow", "Cursor Agent: strengths and workflow", "When to use which (or both)"]),
    ("Windsurf vs Cursor vs Claude Code 2026", "windsurf-vs-cursor-vs-claude-code-2026",
     "Windsurf, Cursor, and Claude Code compared for 2026: pricing, agentic features, and which AI coding tool fits your team.",
     "Three strong options for AI-native development. We compare Windsurf, Cursor, and Claude Code so you can pick the right fit for agentic workflows and team scale.",
     ["Pricing and plans", "Agentic and multi-file support", "Best for: teams, solo, enterprise"]),
    ("Tabnine vs Cursor vs Copilot: which fits your stack?", "tabnine-vs-cursor-vs-copilot-2026",
     "Tabnine vs Cursor vs GitHub Copilot in 2026: privacy, pricing, and where each AI coding tool shines.",
     "Tabnine emphasizes on-prem and privacy; Cursor and Copilot lead on agentic and ecosystem. We compare so you can choose.",
     ["Tabnine: privacy and control", "Cursor and Copilot: ecosystem and agentic", "Choosing by team size and compliance"]),
    ("Replit AI vs Cursor: best for learning and shipping in 2026", "replit-ai-vs-cursor-2026",
     "Replit AI vs Cursor in 2026: which is better for learning, side projects, and shipping full apps with AI.",
     "Replit is all-in-one in the browser; Cursor is a desktop IDE. We compare them for learners and indie builders in 2026.",
     ["Replit: browser-based, all-in-one", "Cursor: IDE-first, agentic", "Best for learning vs best for shipping"]),
    ("Lovable vs Cursor: AI app builders vs AI IDEs", "lovable-vs-cursor-2026",
     "Lovable vs Cursor in 2026: AI app builders vs AI IDEs. When to use a no-code AI builder vs an agentic coding environment.",
     "Lovable targets fast app prototyping; Cursor targets full control in code. We compare so you can pick the right tool for the job.",
     ["Lovable: AI app builder", "Cursor: AI-native IDE", "Use both in the same stack"]),
    ("DevEx stack 2026: agentic workflows and modern tooling", "devex-stack-2026",
     "Build your 2026 DevEx stack: agentic workflows, Cursor, Claude Code, and tooling that keeps architectural integrity.",
     "Developer experience in 2026 means agentic workflows, clear tool choices, and pipelines that don’t get in the way. We outline a practical stack.",
     ["What belongs in a 2026 DevEx stack", "Agentic tooling: Cursor, Claude Code, and more", "Security and CI/CD in the loop"]),
    ("Best agentic coding tools 2026 (multi-agent, orchestration)", "best-agentic-coding-tools-2026",
     "Best agentic coding tools in 2026: multi-agent setups, orchestration, and tools that ship whole features, not just completions.",
     "The top 1% are using multi-agent and orchestrated workflows. We list the tools that actually support that in 2026.",
     ["What makes a tool “agentic” in 2026", "Top tools: Cursor, Claude Code, and ecosystem", "How to get started"]),
    ("How to run agentic workflows with Cursor and Claude Code", "agentic-workflows-cursor-claude-2026",
     "Run agentic workflows with Cursor and Claude Code in 2026: setup, patterns, and tools that plug in.",
     "Step-by-step: how we run agentic workflows using Cursor and Claude Code, and what we add to ship faster.",
     ["Defining your agentic workflow", "Cursor + Claude Code in practice", "Extending with MCP and other tools"]),
    ("Multi-agent coding in 2026: setup and tool stack", "multi-agent-coding-2026",
     "Multi-agent coding in 2026: how to set it up, which tools support it, and a practical stack for teams.",
     "Multi-agent coding is moving from experiment to production. We cover setup and a minimal tool stack for 2026.",
     ["What multi-agent coding means in practice", "Tool stack: IDEs, CLIs, orchestration", "Getting from zero to first run"]),
    ("Diff-based workflows: moving beyond blind AI rewrites", "diff-based-workflows-ai-2026",
     "Diff-based workflows in 2026: move from “blind” AI rewrites to controlled, reviewable patches and merges.",
     "AI can change a lot of code at once. Diff-based workflows keep changes visible and reviewable so you keep control.",
     ["Why diff-based workflows matter", "How to implement them in your stack", "Tools that support review and apply"]),
    ("Cursor Agent mode vs Claude Code CLI: when to use which", "cursor-agent-vs-claude-code-cli-2026",
     "Cursor Agent vs Claude Code CLI: when to use which in 2026, and how they complement each other.",
     "Both do agentic, multi-step tasks. We compare Cursor Agent and Claude Code CLI so you can choose or combine them.",
     ["Cursor Agent: in-IDE, multi-file", "Claude Code CLI: terminal-first", "When to use which"]),
    ("Onboarding devs in hours: AI context windows and time-to-first-commit", "developer-onboarding-ai-2026",
     "Onboard developers in hours using AI context windows and repo-level understanding. Cut time-to-first-commit in 2026.",
     "AI that understands the whole repo can get new devs to first commit in hours instead of weeks. We outline how.",
     ["The old vs new onboarding curve", "AI context and repo-level understanding", "Tools and practices that work"]),
    ("How to ship faster with Cursor and Claude Code in 2026", "ship-faster-cursor-claude-2026",
     "Ship faster with Cursor and Claude Code in 2026: workflows, tooling, and one recommended addition to your stack.",
     "Practical tips to ship faster using Cursor and Claude Code—and how we tighten the loop with one more tool.",
     ["Workflow habits that actually speed you up", "Cursor and Claude Code in the loop", "One addition we recommend"]),
    ("Best VS Code AI extensions 2026 (Copilot, Cursor, Tabnine, etc.)", "best-vs-code-ai-extensions-2026",
     "Best VS Code AI extensions in 2026: Copilot, Cursor, Tabnine, and more. Compare inline completion and agentic options.",
     "VS Code stays central for many devs. We compare the leading AI extensions so you can pick or combine.",
     ["Inline completion: Copilot, Tabnine, and others", "Agentic and chat: Cursor and beyond", "Our recommendation for 2026"]),
    ("AI pair programming: Cursor, Copilot, Claude Code compared", "ai-pair-programming-2026",
     "AI pair programming in 2026: how Cursor, Copilot, and Claude Code compare for real-time assistance and collaboration.",
     "AI pair programming is table stakes in 2026. We compare how Cursor, Copilot, and Claude Code support it.",
     ["What “AI pair programming” means in 2026", "Cursor vs Copilot vs Claude Code", "Picking the right partner"]),
    ("Setting up your AI dev stack in 2026 (step-by-step)", "ai-dev-stack-setup-2026",
     "Set up your AI dev stack in 2026: step-by-step from IDE and CLI to agentic workflows and one recommended add-on.",
     "A minimal, repeatable setup for an AI-native dev stack: Cursor or VS Code, Claude Code CLI, and tools that plug in.",
     ["Step 1: IDE and primary AI", "Step 2: CLI and agentic", "Step 3: extend and ship faster"]),
    ("Security-first CI/CD: secret scanning and dependency checks in 2026", "security-first-cicd-2026",
     "Security-first CI/CD in 2026: automate secret scanning and dependency checks in every branch and pipeline.",
     "AI-assisted dev moves fast; pipelines need to catch secrets and vulnerable deps. We outline a security-first CI/CD setup.",
     ["Why security belongs in every pipeline", "Secret scanning: tools and integration", "Dependency and SBOM checks"]),
    ("DevSecOps for AI-assisted development: what to automate", "devsecops-ai-development-2026",
     "DevSecOps for AI-assisted development in 2026: what to automate so speed and security stay aligned.",
     "When AI helps write and change code, DevSecOps has to keep up. We cover what to automate first.",
     ["Where AI-assisted dev changes risk", "Automation that actually helps", "Tooling and pipeline patterns"]),
    ("Best secret scanning tools for dev teams 2026", "secret-scanning-tools-devops-2026",
     "Best secret scanning tools for dev teams in 2026: pre-commit, CI, and repo-wide coverage.",
     "Secrets in code are still a top vector. We compare secret scanning tools that fit modern dev and CI.",
     ["What to look for in a secret scanner", "Leading tools and integration points", "Recommendations by team size"]),
    ("Dependency scanning in CI: tools and best practices 2026", "dependency-scanning-ci-2026",
     "Dependency scanning in CI in 2026: tools, SBOM, and best practices for every merge and release.",
     "Dependency and supply-chain risk belong in CI. We cover tools and practices that work in 2026.",
     ["Why dependency scanning in CI", "Tools and SBOM integration", "Best practices and rollout"]),
    ("Best hosting for side projects and dev portfolios 2026", "best-hosting-for-developers-2026",
     "Best hosting for side projects and dev portfolios in 2026: fast, simple, and developer-friendly options.",
     "Where to host side projects and portfolios in 2026 without overpaying or over-engineering.",
     ["What developers need from hosting", "Top options for 2026", "Picking by project type"]),
    ("Deploying AI apps: from Cursor/Replit to production", "deploy-ai-apps-production-2026",
     "Deploy AI apps from Cursor and Replit to production in 2026: paths, hosting, and a simple pipeline.",
     "You built it with AI; now ship it. We outline deployment paths from Cursor and Replit to production.",
     ["From local/Replit to first deploy", "Hosting and runtimes that fit", "CI and repeatable deploys"]),
    ("Best MCP servers for Cursor and Claude Code 2026", "best-mcp-servers-cursor-claude-2026",
     "Best MCP servers for Cursor and Claude Code in 2026: extend your AI stack with tools, APIs, and data.",
     "MCP lets Cursor and Claude Code call tools and data. We list MCP servers that are worth adding in 2026.",
     ["What MCP adds to your stack", "Servers we use and recommend", "How to add and configure them"]),
    ("Cursor rules and AI context: how to get better results", "cursor-rules-best-practices-2026",
     "Cursor rules and AI context in 2026: how to write rules and provide context so you get better, consistent results.",
     "Good rules and context make Cursor (and similar tools) much more useful. We share what works.",
     ["Why rules and context matter", "Writing effective Cursor rules", "Context: repo, docs, and scope"]),
    ("Claude Code CLI tips and workflows for 2026", "claude-code-cli-tips-2026",
     "Claude Code CLI tips and workflows for 2026: get the most from terminal-first agentic coding.",
     "Claude Code CLI is powerful when you know the patterns. We share tips and workflows we use in 2026.",
     ["Install and first run", "Workflows that save time", "Integrating with Cursor and the rest of the stack"]),
]

def escape_json(s):
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")

def build_article(title, slug_stem, meta_desc, intro, sections):
    slug = slug_stem + ".html"
    url = f"{BASE}/{slug}"
    safe_title = title.replace('"', '\\"')
    safe_meta = meta_desc.replace('"', '\\"')
    safe_intro = intro.replace('"', '\\"')

    body_sections = "\n".join(
        f"""            <h2>{h}</h2>
            <p>This section will cover {h.lower()} in detail. Expand with your own research and experience—and add your BrainGrid (or other) affiliate links where relevant.</p>"""
        for h in sections
    )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Code Pipelines</title>
    <meta name="description" content="{escape_json(meta_desc)}">
    <link rel="canonical" href="{url}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="{url}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{escape_json(meta_desc)}">
    <meta property="og:locale" content="en_US">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{escape_json(meta_desc)}">
    <style>
{STYLES}
    </style>
</head>
<body>
    <a href="#main" class="skip-link">Skip to main content</a>
    <header>
{NAV}
    </header>
    <main id="main">
        <article>
            <h1>{title}</h1>
            <p class="meta">{DATE} · Code Pipelines</p>

            <p>{intro}</p>

{body_sections}

{CTA}
        </article>
    </main>
    <footer>
        <p><a href="/">Code Pipelines</a> · <a href="/blog/">Blog</a></p>
    </footer>

    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "{escape_json(title)}",
        "description": "{escape_json(meta_desc)}",
        "url": "{url}",
        "datePublished": "{DATE}",
        "publisher": {{
            "@type": "Organization",
            "name": "Code Pipelines",
            "url": "https://codepipelines.com/"
        }}
    }}
    </script>
</body>
</html>
"""
    return slug, html

def main():
    os.makedirs(BLOG_DIR, exist_ok=True)
    generated = []
    for title, slug_stem, meta_desc, intro, sections in ARTICLES:
        slug, html = build_article(title, slug_stem, meta_desc, intro, sections)
        path = os.path.join(BLOG_DIR, slug)
        with open(path, "w") as f:
            f.write(html)
        generated.append((slug, title))
        print("Wrote", slug)
    # Write sitemap lines and blog index entries to a temp file for manual merge, or append to sitemap
    with open(os.path.join(BLOG_DIR, "_generated_list.txt"), "w") as f:
        for slug, title in generated:
            f.write(f"https://codepipelines.com/blog/{slug}\n")
    print("Done. See blog/_generated_list.txt for sitemap URLs.")

if __name__ == "__main__":
    main()
