# PatentForge Prompts — User Manual

**For anyone, regardless of technical background.**

> This tool is not legal advice. It is a research assistant that helps you organize your thinking before talking to a patent attorney. The author is not a lawyer. Always consult a registered patent attorney before making any filing decisions.

---

## What Is This?

PatentForge Prompts is a free set of instructions (called "prompts") that you copy and paste into an AI chatbot. The chatbot then walks you through a six-step research process to help you understand whether your invention idea might be patentable — and what to do next.

Think of it like a structured interview. You describe your invention, and the AI asks the right questions, searches for similar inventions that already exist, checks your idea against patent law requirements, and produces a plain-English report you can take to a patent attorney.

**What it is:** A research tool that helps you prepare before spending money on legal advice.

**What it is not:** Legal advice, a patent application, or a substitute for a patent attorney.

---

## What You Need Before You Start

1. **A paid AI chatbot subscription** — one of the following:
   - **Claude Pro** ($20/month) at [claude.ai](https://claude.ai) — recommended
   - **Claude Max** or **Claude Team** at [claude.ai](https://claude.ai)
   - **Gemini Advanced** ($20/month) at [gemini.google.com](https://gemini.google.com)

   Free versions of these chatbots will not work well. They lack the web search and memory capacity that the later stages require.

2. **Your invention description** — a written explanation of what your invention does, how it works, and what makes it different from what already exists. The more detail you provide, the better the analysis. Even a few paragraphs will work, but a page or two of technical detail produces much stronger results.

3. **The prompt files** — download them from [github.com/scottconverse/patentforge-prompts](https://github.com/scottconverse/patentforge-prompts). Click the green "Code" button, then "Download ZIP." Unzip the folder on your computer.

---

## How to Run the Analysis (Step by Step)

The analysis has six stages. Each stage builds on the one before it. You only need to open one file yourself — after that, the system handles the connections between stages automatically.

### Stage 1: Technical Intake

This stage takes your invention description and restates it in precise technical language.

1. Open the file called `Stage-1-Technical-Intake.md` on your computer (any text editor works — Notepad, TextEdit, or even a web browser)
2. Select everything inside the file and copy it (Ctrl+C on Windows, Cmd+C on Mac)
3. Go to [claude.ai](https://claude.ai) or [gemini.google.com](https://gemini.google.com) and start a **new conversation**
4. Paste the copied text into the chat box (Ctrl+V or Cmd+V)
5. After the pasted text, type or paste your invention description
6. Press Enter to send

The AI will analyze your description and produce a structured technical summary. At the very end of its response, you will see a block of text marked with a line that says something like:

```
========== COPY EVERYTHING BELOW THIS LINE INTO A NEW CONVERSATION ==========
```

### Stage 2: Prior Art Search

This stage searches the internet for existing patents, research papers, and products that are similar to your invention.

1. Copy everything from the "COPY" line to the end of the AI's response
2. Open a **new conversation** (do not continue in the same one)
3. Paste the copied text and press Enter

The AI will search patent databases, academic papers, and product listings. This is where having a paid subscription with web search matters most — without it, the AI can only guess from memory, which is unreliable.

### Stages 3 through 5

Each of these stages works the same way:

1. Wait for the AI to finish
2. Find the "COPY EVERYTHING BELOW THIS LINE" marker at the end
3. Copy everything from that line to the end
4. Open a **new conversation**
5. Paste and press Enter

- **Stage 3** (Patentability Analysis) checks your invention against patent law requirements
- **Stage 4** (Deep Dive) goes deeper into the specific technology areas that matter for your invention
- **Stage 5** (IP Strategy) provides filing recommendations and cost estimates

### Stage 6: Final Report

Same process one last time. After Stage 6 finishes, you have your complete patent analysis report. There is no more copying or pasting — you are done.

---

## What to Do with Your Report

The report is a research document, not a legal opinion. Here is what to do with it:

1. **Read the Overall Landscape Assessment** — this tells you whether the research suggests your invention has a path to a patent, or whether there are significant obstacles.

2. **Review the risk scores** — each area of patent law gets a score from 0 to 100. Higher scores mean higher risk. Pay attention to anything above 60.

3. **Take it to a patent attorney** — print the report or save it as a PDF and bring it to a consultation with a registered patent attorney. The report gives the attorney a head start, which can save you time and money. Many patent attorneys offer free or low-cost initial consultations.

4. **Do not file a patent application based on this report alone.** The report is a starting point for a conversation with a professional, not a replacement for one.

---

## Common Problems and Solutions

**Problem: The AI says it cannot search the web.**
Solution: You may be using a free-tier chatbot. Upgrade to Claude Pro or Gemini Advanced. If you already have a paid subscription, check that web search is turned on in your chatbot's settings.

**Problem: The AI's response gets cut off in the middle.**
Solution: Type "continue" and press Enter. The AI will pick up where it left off. If it keeps cutting off, you may be using a chatbot with a context window that is too small — switch to Claude Pro or Gemini Advanced.

**Problem: The handoff block is missing or incomplete.**
Solution: Type "Please regenerate the handoff block" and press Enter. The AI will produce it again.

**Problem: A stage produces different results when I run it again.**
Solution: This is normal. AI chatbots produce slightly different responses each time. The core findings should be consistent, but exact wording and risk scores may vary by a few points.

**Problem: The report says my invention is not patentable.**
Solution: The report reflects what the AI found in its research, but it is not the final word. A patent attorney may identify angles the AI missed. Consider consulting one before giving up.

**Problem: I do not understand the technical language in the report.**
Solution: Look at the Plain-English Summary section (Section 10 of the final report). It explains everything in everyday language. You can also check the glossary below.

---

## Glossary

**Prior art** — anything that already exists and is publicly known that is similar to your invention. This includes patents, published papers, products for sale, YouTube videos, blog posts, or anything else that was publicly available before your filing date.

**Patentability** — whether an invention meets the legal requirements for getting a patent. In the United States, an invention must be new, non-obvious, and useful.

**Section 101 (101)** — the part of U.S. patent law that says what kinds of things can be patented. Abstract ideas, laws of nature, and natural phenomena cannot be patented on their own. Software and AI inventions sometimes run into trouble here.

**Section 102 (102)** — the part of U.S. patent law that requires your invention to be new (called "novelty"). If someone else already invented the same thing and made it public, you cannot patent it.

**Section 103 (103)** — the part of U.S. patent law that says your invention cannot be "obvious." Even if nobody has built your exact invention before, if a skilled person in your field would have thought of it easily by combining existing ideas, it may not be patentable.

**Section 112 (112)** — the part of U.S. patent law that requires you to describe your invention clearly enough that someone skilled in your field could build it. You also need to clearly define what you are claiming as your invention.

**Provisional patent application** — a simpler, cheaper patent filing that gives you a filing date and 12 months to file a full (non-provisional) application. It costs around $320 for small entities. It is not examined and does not become a patent on its own.

**Non-provisional patent application** — the full patent application that gets examined by the USPTO. This is what actually becomes a patent if approved. It costs significantly more and typically requires a patent attorney to prepare.

**CPC codes** — Cooperative Patent Classification codes. These are category labels that the patent office uses to organize patents by technology area. They help you find related patents during a prior art search.

**USPTO** — the United States Patent and Trademark Office, the government agency that examines and grants patents.

**Claims** — the specific legal statements in a patent application that define exactly what the patent covers. Think of them as the boundary lines of your patent's territory.

**Freedom to operate (FTO)** — whether you can make, use, or sell your invention without infringing on someone else's existing patent. Having your own patent does not automatically mean you have freedom to operate.

**Filing landscape assessment** — the report's overall conclusion about whether the research suggests conditions are favorable for filing a patent application, based on the prior art found and the legal analysis performed.

---

*PatentForge Prompts v1.2.0 — April 2026*
*This is a research tool, not legal advice. Always consult a registered patent attorney.*
