# PatentForge Prompts

> **This tool is NOT legal advice.** PatentForge Prompts is an AI-powered research tool that helps inventors organize their thinking before consulting a patent attorney. It does not create an attorney-client relationship. The author is not a lawyer. Always consult a registered patent attorney before making filing decisions. See [LEGAL_NOTICE.md](LEGAL_NOTICE.md) and [Terms of Service](docs/terms.html) for full details.

**License:** [CC BY-SA 4.0](LICENSE) — derivative works must retain all legal disclaimers.

**A 6-stage AI prompt pipeline that turns an invention description into a comprehensive patent feasibility analysis.**

**Version 1.2.0** — April 2026

No software to install. No API keys to configure. Just copy one prompt, paste it into an AI chatbot, describe your invention, and go. Each stage automatically produces the input for the next stage — one copy-paste per stage, six total.

---

## Choose your PatentForge tier

| | What it is | Best for |
|---|---|---|
| **PatentForge Prompts** — you are here | 6 prompts you paste into any AI (Claude, Gemini Advanced). No install, no API keys, no cost beyond your chatbot subscription. | Inventors who want to try the analysis pipeline before committing to a desktop install, or who already have a paid Claude / Gemini plan and prefer a browser workflow. |
| **[PatentForge](https://github.com/scottconverse/patentforge)** | Desktop app (Windows / macOS / Linux). Runs locally on Ollama + Gemma 4 (fully offline, free) or with the Anthropic Claude API (cloud, your key). Adds 3-agent claim drafting, 5-agent patent-application generation, USPTO PatentSearch integration, compliance checks, Word/HTML/Markdown exports. | Inventors who want privacy (local mode never leaves your hardware), or who want the full claim-drafting / application-generation workflow beyond just feasibility analysis. |

Both tiers share the same 6-stage feasibility analysis pattern. The prompts here are the no-install entry tier; PatentForge adds the workflow surface around them.

---

## Recommended Setup

These prompts were developed, tested, and tuned on **Anthropic's Claude**. The preferred setup is:

- **A paid Claude account** (Pro, Max, or Team) at [claude.ai](https://claude.ai)
- **Claude's built-in web search** — required for Stage 2 (prior art research) and beneficial for Stages 3-4
- **Claude's extended context window** — by Stage 6, all previous outputs are fed in as input, which requires a large context window

Claude Pro also includes features like Projects (for saving your prompts), Cowork mode, and the Claude Chrome Extension, which can streamline the workflow.

### Google Gemini

**Gemini Advanced** (paid) is also a strong option for these prompts. Gemini has built-in web search with Google's search infrastructure, a large context window, and good analytical depth. If you don't have a Claude account, Gemini Advanced is a solid alternative.

### Why Claude and Gemini?

Both Claude and Gemini offer **1 million+ token context windows** — which is essential for this pipeline. By Stage 6, you're feeding in all five previous stage outputs as input, which can easily exceed 100K tokens. Other LLMs like ChatGPT, Grok, and Perplexity have significantly smaller context windows and will choke, truncate, or degrade on the later stages.

### Other LLMs

These prompts can technically be used with other paid-tier LLMs that have live web search — such as ChatGPT Plus or Perplexity Pro — but they are **not recommended**. Beyond not being tested or tuned for those platforms, their smaller context windows mean the later stages (especially Stage 6) may fail, truncate, or produce incomplete results.

### Why Not Free-Tier LLMs?

**Free-tier LLMs are not recommended.** Stage 2 requires live web search to find real patents, papers, and products. Without it, the AI generates prior art references from memory, which often means fabricated patent numbers, hallucinated papers, and stale results. That bad data then cascades through every subsequent stage — producing a report that looks professional but contains unreliable information. For patent work, that's worse than no analysis at all.

---

## How It Works

You describe your invention once. The system runs 6 stages in sequence. Each stage automatically produces a **handoff block** — a ready-to-paste package containing everything the next stage needs. You just copy it and paste it into a new conversation.

| Stage | File | What It Does |
|-------|------|-------------|
| 1 | `Stage-1-Technical-Intake.md` | Restates your idea in precise patent-ready technical language |
| 2 | `Stage-2-Prior-Art-Search.md` | Searches patents, papers, products, and GitHub for existing work |
| 3 | `Stage-3-Patentability-Analysis.md` | Full §101/§102/§103/§112 statutory analysis with risk ratings |
| 4 | `Stage-4-Deep-Dive-Analysis.md` | Specialized deep analysis of the most patentable and riskiest elements |
| 5 | `Stage-5-IP-Strategy.md` | Filing recommendations, cost estimates, claim strategy |
| 6 | `Stage-6-Final-Report.md` | Assembles everything into one comprehensive 10-section report |

**You only open one file: Stage 1.** After that, each stage hands off to the next automatically.

---

## Quick Start

### What You Need

- **A paid Claude account** (Pro, Max, or Team) with web search enabled — or Gemini Advanced. Both have the 1M+ token context window required for the later stages.
- **Your invention description** — the more technical detail you provide, the better the analysis

### Step by Step

**Stage 1 (the only manual setup):**
1. Open `Stage-1-Technical-Intake.md`
2. Copy everything inside the code block
3. Paste it into a **new Claude conversation**
4. After the prompt, type or paste your **invention description**
5. Send it

**Stage 2:**
1. Claude produces a Stage 1 analysis, then a **handoff block** marked with:
   `========== COPY EVERYTHING BELOW THIS LINE INTO A NEW CONVERSATION ==========`
2. Copy everything from that line to the end marker
3. Open a **new Claude conversation**
4. Paste the handoff block and send it

**Stages 3 through 5:**
- Same process: copy the handoff block, open new conversation, paste, send
- Each handoff carries forward ALL previous stage outputs automatically

**Stage 6 (Final Report):**
- Same process one last time
- The output is your complete patent analysis report — no more handoffs

**That's it. One file to open. One copy-paste per stage. Six stages total.**

---

## Writing a Good Invention Description

The better your input, the better your analysis. Include as much of the following as you can:

- **What it does** — The problem it solves and for whom
- **How it works** — Architecture, algorithms, data flows, mechanical design, materials
- **What makes it different** — Why existing solutions don't do what yours does
- **What's built vs. conceptual** — Have you built a prototype, or is this still an idea?
- **Specific technologies** — AI models, sensors, manufacturing processes, materials, software frameworks

A few sentences will produce a basic analysis. A detailed technical description will produce a much stronger one.

---

## Execution Lanes

You don't have to run all 6 stages every time. Here are some useful shortcuts:

| Lane | Stages | Use When |
|------|--------|----------|
| **Full Analysis** | 1 → 2 → 3 → 4 → 5 → 6 | Complete patent feasibility assessment |
| **Quick Assessment** | 1 → 3 → 5 | Fast patentability check (skips deep prior art search) |
| **Prior Art Only** | 1 → 2 | Just want to know what's already out there |
| **Strategy Only** | 1 → 5 | Already know the landscape, need filing guidance |

For shortcut lanes, open the relevant Stage file directly and paste your previous outputs after it.

---

## Which Stages Need Web Search?

| Stage | Web Search | Why |
|-------|-----------|-----|
| 1 — Technical Intake | Not needed | Pure analysis of your description |
| 2 — Prior Art Search | **Required** | Must search real patent databases, papers, products. If unavailable, the prompt will warn you and mark all references as unverified. |
| 3 — Patentability Analysis | Helpful | Can look up recent case law and USPTO guidance. Without it, legal references are caveated as training-data-only. |
| 4 — Deep Dive | Helpful | Can search domain-specific patent landscape. Without it, landscape analysis is caveated. |
| 5 — IP Strategy | Not needed | Synthesis and recommendations from prior stages |
| 6 — Final Report | Not needed | Assembles and synthesizes all previous outputs |

Stage 2 is the critical one. If your AI doesn't have live web search, the prior art results will be unreliable, and that unreliability cascades through every subsequent stage.

---

## Cost

**No additional cost.** With a Claude Pro ($20/month), Claude Max, Claude Team, or Gemini Advanced ($20/month) subscription, running these prompts is included in your subscription. There are no per-run charges, no API fees, and no token costs. You're just using your chatbot.

---

## Customizing the Prompts

Every prompt is a plain text file. You can edit them to:

- Add industry-specific guidance for your field
- Adjust the output length or detail level
- Add or remove analysis sections
- Change the writing style or tone
- Focus on specific patent offices (these default to U.S. patent law)

---

## What the Analysis Covers

### For All Inventions
- Technical restatement in patent-ready language
- Prior art search across patents, papers, products, and open source
- Full patentability assessment (§101, §102, §103, §112)
- Common examiner concerns analysis for this technology area
- Filing strategy (provisional vs. non-provisional, timing, costs)
- Claim direction recommendations
- Risk scoring (0-100) for each statutory category
- Documentation checklist
- Plain-English summary anyone can understand

### Special Depth for AI/ML Inventions
- Patent zone classification (strong vs. red-flag categories)
- Alice/Mayo §101 deep analysis specific to AI
- Current USPTO AI guidance and Federal Circuit decisions
- AI claim framing strategy (system vs. method vs. CRM)
- Trade secret vs. patent boundary analysis for algorithms

### Special Depth for 3D Printing Inventions
- Design patent vs. utility patent analysis
- Category classification (geometry, process, material, software, post-processing)
- 3D printing patent landscape search
- Design patent claiming strategy
- Combined AI + 3D printing opportunities

---

## File List

```
PatentForge Prompts/
+-- README.md                              This file
+-- 00-common-rules.md                     Reference only (rules are baked into each stage)
+-- Stage-1-Technical-Intake.md            START HERE — paste into Claude + add your description
+-- Stage-2-Prior-Art-Search.md            Auto-generated by Stage 1 handoff (or use directly)
+-- Stage-3-Patentability-Analysis.md      Auto-generated by Stage 2 handoff (or use directly)
+-- Stage-4-Deep-Dive-Analysis.md          Auto-generated by Stage 3 handoff (or use directly)
+-- Stage-5-IP-Strategy.md                 Auto-generated by Stage 4 handoff (or use directly)
+-- Stage-6-Final-Report.md                Auto-generated by Stage 5 handoff (or use directly)
```

**Normal workflow:** You only need to open `Stage-1-Technical-Intake.md`. Everything else flows through the handoff system.

**Shortcut lanes or re-runs:** Open the individual stage file directly and paste your previous stage outputs after it.

---

## What's New in v1.2.0

**Reliability improvements based on a full forensic audit and 6-stage stress test.**

- **Web search fallback (Stage 2)** — If web search isn't available, Stage 2 now warns you explicitly and marks all references as unverified instead of silently generating unreliable results. If you proceed anyway, a warning banner flags every reference as training-data-only.
- **URL verification for prior art (Stage 2)** — Every reference now requires a verifiable URL. References without one are marked (UNVERIFIED) so downstream stages can treat them with appropriate caution.
- **Prior art verification gate (Stage 3)** — Before analyzing novelty, Stage 3 now checks whether prior art references include verifiable URLs and caveats any conclusions based on unverified references.
- **Legal reference caveats (Stage 3)** — When web search isn't available, Stage 3 notes that legal references come from training data and may not reflect the most recent case law.
- **Web search language aligned (Stage 4)** — Changed from "requires web search" to "benefits from web search" with a graceful fallback, matching the actual requirement level.
- **Cost estimate date stamp (Stage 5)** — Cost estimates now include "(as of 2025)" and a link to verify current USPTO fees, preventing stale data.
- **Minimum input threshold (Stage 1)** — If your invention description is fewer than 50 words, Stage 1 now asks for more detail before proceeding instead of producing a weak analysis.
- **Truncation safeguards (Stages 3-5)** — Handoff blocks now include priority instructions: if output space runs low, the next-stage prompt is always preserved first, preventing corrupted handoffs.
- **Word count target (Stage 2)** — Added a 1,500-3,000 word target for consistent output length.

---

---

*Developed and tested on Anthropic's Claude. Gemini Advanced is a supported alternative. Other LLMs lack the context window size required for later stages. Free-tier LLMs are not recommended. v1.2.0 — April 2026. Part of the [PatentForge](https://github.com/scottconverse/patentforge) family.*
