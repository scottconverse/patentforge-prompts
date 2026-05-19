# Changelog

All notable changes to PatentForge Prompts (formerly Patent Analyzer Prompts; renamed 2026-05-19) will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2026-04-07

### Changed
- All 6 stage prompts synced to PromptTemplates.cs source of truth from patent-analyzer-app
- All 6 stage prompts now position the AI as an "AI-powered research assistant" rather than a "patent attorney" or "patent strategist"
- Every stage output now begins with a mandatory disclaimer identifying the output as AI-generated research, not legal advice
- Section titles softened to reflect landscape analysis rather than legal directives:
  - "File or Don't File" is now "Filing Landscape Assessment"
  - "Bottom-Line Recommendation" is now "Overall Landscape Assessment"
  - "Examiner Rejection Simulation" is now "Common Examiner Concerns in This Technology Area"
  - "Freedom-to-Operate Flag" is now "Potential Blocking IP to Discuss with Counsel"
- Assessment labels updated:
  - "FILE NOW" is now "LANDSCAPE FAVORS FILING"
  - "DO NOT FILE" is now "SIGNIFICANT OBSTACLES IDENTIFIED"
  - "DOCUMENT MORE" is now "MORE DOCUMENTATION WOULD STRENGTHEN POSITION"
  - "DESIGN PATENT ONLY" is now "DESIGN PATENT AVENUE WORTH EXPLORING"
- Stage 3 patentability analysis sections now include explicit "Start with a one-sentence plain-English intro" instructions for each statutory requirement (§101, §102, §103, §112)
- Stage 3 §101 analysis expanded with AI-specific and 3D printing-specific guidance for risk ratings
- Stage 4 subsections renamed for clarity: "Strongest Patentable Elements", "Weakest Elements — Be Honest", "Claim Framing Strategy"
- Stage 5 Section G (Blocking IP) rewritten to avoid implying FTO opinion: now instructs AI to note dominant patents relevant to commercialization and flag concerns for attorney discussion
- Stage 5 Section H (Overall Landscape Assessment) updated to numbered list (1-5) format with "KEEP AS TRADE SECRET" replacing "TRADE SECRET PROTECTION MAY BE MORE APPROPRIATE"
- Stage 5 Section I (Plain-English Summary) now requires specific questions: landscape outlook, biggest obstacle, next step, rough cost
- Stage 5 Cost table reformatted to `| Item | Small Entity Cost | Timeline |` with 2-4 year issuance timeline
- Stage 5 Filing Landscape Assessment now explicitly handles narrow protectability scenarios and trade secret tradeoffs
- Stage 6 Section 3 restructured with numbered subsections (3.1 Closest Prior Art References, 3.2 Element Comparison Matrix, 3.3 White Space & Density) each with plain-English intros
- Stage 6 Section 4 subsections each include specific plain-English introductory sentences
- Stage 6 Section 5 (Deep Dive) now includes explicit instruction not to create sections for domains not present in the invention
- Stage 6 Section 6 (IP Strategy) table for 6.1 Protection Mix uses Component | Recommended Protection | Rationale | Duration format
- Stage 6 Section 9 closing now requires: "This assessment should be reviewed by a registered patent attorney before any filing decisions are made."
- Stage 6 closing disclaimer updated to explicitly state "The author of this tool is not a lawyer. The AI system that generated this analysis is not a lawyer."
- Stage 6 length budget rule updated: "BUDGET YOUR LENGTH: Sections 1-6 should total no more than 3500 words"
- Common rules (00-common-rules.md) updated with full Section Introductions examples

### Added
- Mandatory disclaimer block in common rules, output at the start of every stage
- Per-stage disclaimer anchors ensuring disclaimers survive copy-paste between conversations
- Stage 5 ⚠️ CRITICAL REQUIREMENT warning block requiring Plain-English Summary for the Inventor section
- Stage 6 ⚠️ CRITICAL REQUIREMENT warning block for Section 10
- Section Introductions examples in common rules reference file
- Stage 1 Section Introductions examples (prior art, §101, white space)
- Stage 2 web search warning revised to appear as banner warning at top of response

### Fixed
- Stage 1 handoff now correctly instructs AI to include ORIGINAL INVENTION DESCRIPTION in handoff block

## [1.1.0] - 2026-03-15

### Added
- Web search fallback warnings in Stage 2
- URL verification for prior art references
- Prior art verification gate in Stage 3
- Legal reference caveats for training-data-only references
- Cost estimate date stamps with USPTO fee verification links
- Minimum 50-word input threshold in Stage 1
- Truncation safeguards in Stages 3-5
- Word count targets for consistent output

### Fixed
- Web search language aligned in Stage 4 (changed from "requires" to "benefits from")

## [1.0.0] - 2026-02-01

### Added
- Initial release: 6-stage patent landscape analysis prompt system
- Stages: Technical Intake, Prior Art Search, Patentability Analysis, Deep Dive, IP Strategy, Final Report
- Handoff block system for multi-conversation workflow
- Common rules for consistent output formatting
- Support for Claude Pro/Max/Team and Gemini Advanced