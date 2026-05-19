"""Generate a professionally formatted PDF for the PatentForge Prompts README."""
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.enums import TA_CENTER

DARK_BLUE = HexColor("#1a237e")
MED_BLUE = HexColor("#283593")
LIGHT_BLUE = HexColor("#e8eaf6")
HEADER_BG = HexColor("#1a237e")
ROW_ALT = HexColor("#f5f5f5")
WHITE = HexColor("#ffffff")
GRAY = HexColor("#666666")
LIGHT_GRAY = HexColor("#e0e0e0")
WARN_BG = HexColor("#fff3e0")
GREEN_BG = HexColor("#e8f5e9")

def build_pdf():
    import os
    output_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "PatentForge-Prompts-README.pdf",
    )
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        topMargin=0.75*inch, bottomMargin=0.75*inch,
        leftMargin=0.85*inch, rightMargin=0.85*inch,
    )
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle("T", parent=styles["Title"],
        fontSize=28, textColor=DARK_BLUE, spaceAfter=6, fontName="Helvetica-Bold")
    subtitle_style = ParagraphStyle("Sub", parent=styles["Normal"],
        fontSize=13, textColor=GRAY, spaceAfter=20, fontName="Helvetica-Oblique")
    h1 = ParagraphStyle("H1", parent=styles["Heading1"],
        fontSize=18, textColor=DARK_BLUE, spaceBefore=20, spaceAfter=10, fontName="Helvetica-Bold")
    h2 = ParagraphStyle("H2", parent=styles["Heading2"],
        fontSize=14, textColor=MED_BLUE, spaceBefore=14, spaceAfter=8, fontName="Helvetica-Bold")
    body = ParagraphStyle("B", parent=styles["Normal"],
        fontSize=10, leading=14, spaceAfter=6, fontName="Helvetica")
    body_bold = ParagraphStyle("BB", parent=body, fontName="Helvetica-Bold")
    bullet = ParagraphStyle("Bul", parent=body,
        leftIndent=20, bulletIndent=8, spaceBefore=2, spaceAfter=2)
    tip_style = ParagraphStyle("Tip", parent=body,
        backColor=LIGHT_BLUE, leftIndent=12, rightIndent=12,
        spaceBefore=6, spaceAfter=6, borderPadding=8)
    warn_style = ParagraphStyle("Warn", parent=body,
        backColor=WARN_BG, leftIndent=12, rightIndent=12,
        spaceBefore=6, spaceAfter=6, borderPadding=8)
    green_style = ParagraphStyle("Green", parent=body,
        backColor=GREEN_BG, leftIndent=12, rightIndent=12,
        spaceBefore=6, spaceAfter=6, borderPadding=8)
    footer_style = ParagraphStyle("Foot", parent=body,
        fontSize=9, textColor=GRAY, fontName="Helvetica-Oblique", alignment=TA_CENTER)
    step_style = ParagraphStyle("Step", parent=body,
        leftIndent=20, spaceBefore=1, spaceAfter=1)

    story = []

    def hr():
        story.append(Spacer(1, 6))
        story.append(HRFlowable(width="100%", thickness=1, color=LIGHT_GRAY))
        story.append(Spacer(1, 6))

    def make_table(headers, rows, col_widths=None):
        data = [headers] + rows
        t = Table(data, colWidths=col_widths, repeatRows=1)
        cmds = [
            ("BACKGROUND", (0, 0), (-1, 0), HEADER_BG),
            ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 10),
            ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
            ("FONTSIZE", (0, 1), (-1, -1), 9),
            ("LEADING", (0, 0), (-1, -1), 13),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("GRID", (0, 0), (-1, -1), 0.5, LIGHT_GRAY),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ("LEFTPADDING", (0, 0), (-1, -1), 8),
            ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ]
        for i in range(1, len(data)):
            if i % 2 == 0:
                cmds.append(("BACKGROUND", (0, i), (-1, i), ROW_ALT))
        t.setStyle(TableStyle(cmds))
        return t

    # ===== TITLE =====
    story.append(Spacer(1, 40))
    story.append(Paragraph("PatentForge Prompts", title_style))
    story.append(Paragraph("v1.2.0", subtitle_style))
    story.append(Paragraph(
        "<b>A 6-stage AI prompt pipeline that turns an invention description into a "
        "comprehensive patent feasibility analysis.</b>", body_bold))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "No software to install. No API keys to configure. Just copy one prompt, paste it into "
        "an AI chatbot, describe your invention, and go. Each stage automatically produces the "
        "input for the next stage \u2014 one copy-paste per stage, six total.", body))
    hr()

    # ===== RECOMMENDED SETUP =====
    story.append(Paragraph("Recommended Setup", h1))
    story.append(Paragraph(
        "These prompts were developed, tested, and tuned on <b>Anthropic\u2019s Claude</b>. "
        "The preferred setup is:", body))
    story.append(Paragraph(
        "\u2022  <b>A paid Claude account</b> (Pro, Max, or Team) at claude.ai", bullet))
    story.append(Paragraph(
        "\u2022  <b>Claude\u2019s built-in web search</b> \u2014 required for Stage 2 (prior art "
        "research) and beneficial for Stages 3\u20134", bullet))
    story.append(Paragraph(
        "\u2022  <b>Claude\u2019s extended context window</b> \u2014 by Stage 6, all previous "
        "outputs are fed in as input, which requires a large context window", bullet))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "Claude Pro also includes features like Projects (for saving your prompts), Cowork mode, "
        "and the Claude Chrome Extension, which can streamline the workflow.", body))

    story.append(Paragraph("Google Gemini", h2))
    story.append(Paragraph(
        "<b>Gemini Advanced</b> (paid) is also a strong option. Gemini has built-in web search "
        "with Google\u2019s search infrastructure, a large context window, and good analytical "
        "depth. If you don\u2019t have a Claude account, Gemini Advanced is a solid alternative.", body))

    story.append(Paragraph("Why Claude and Gemini?", h2))
    story.append(Paragraph(
        "Both Claude and Gemini offer <b>1 million+ token context windows</b> \u2014 which is "
        "essential for this pipeline. By Stage 6, you\u2019re feeding in all five previous stage "
        "outputs as input, which can easily exceed 100K tokens. Other LLMs like ChatGPT, Grok, "
        "and Perplexity have significantly smaller context windows and will choke, truncate, or "
        "degrade on the later stages.", tip_style))

    story.append(Paragraph("Why Not Free-Tier LLMs?", h2))
    story.append(Paragraph(
        "<b>Free-tier LLMs are not recommended.</b> Stage 2 requires live web search to find real "
        "patents, papers, and products. Without it, the AI generates prior art references from "
        "memory, which often means fabricated patent numbers, hallucinated papers, and stale results. "
        "That bad data cascades through every subsequent stage \u2014 producing a report that "
        "looks professional but contains unreliable information. For patent work, that\u2019s worse "
        "than no analysis at all.", warn_style))
    hr()

    # ===== HOW IT WORKS =====
    story.append(Paragraph("How It Works", h1))
    story.append(Paragraph(
        "You describe your invention once. The system runs 6 stages in sequence. Each stage "
        "automatically produces a <b>handoff block</b> \u2014 a ready-to-paste package containing "
        "everything the next stage needs. You just copy it and paste it into a new conversation.", body))
    story.append(Spacer(1, 6))
    story.append(make_table(
        ["Stage", "What It Does"],
        [
            ["1 \u2014 Technical Intake", "Restates your idea in precise patent-ready technical language"],
            ["2 \u2014 Prior Art Search", "Searches patents, papers, products, and GitHub for existing work"],
            ["3 \u2014 Patentability Analysis", "Full \u00a7101/\u00a7102/\u00a7103/\u00a7112 statutory analysis with risk ratings"],
            ["4 \u2014 Deep Dive", "Specialized deep analysis of the most patentable and riskiest elements"],
            ["5 \u2014 IP Strategy", "Filing landscape assessment, cost estimates, claim strategy"],
            ["6 \u2014 Final Report", "Assembles everything into one comprehensive 10-section report"],
        ],
        col_widths=[2*inch, 4.5*inch]
    ))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "<b>You only open one file: Stage 1.</b> Everything else flows through the handoff system.",
        green_style))
    hr()

    # ===== QUICK START =====
    story.append(Paragraph("Quick Start", h1))

    story.append(Paragraph("What You Need", h2))
    story.append(Paragraph(
        "\u2022  <b>A paid Claude account</b> (Pro, Max, or Team) with web search enabled \u2014 "
        "or Gemini Advanced. Both have the 1M+ token context window required.", bullet))
    story.append(Paragraph(
        "\u2022  <b>Your invention description</b> \u2014 the more technical detail, the better", bullet))

    story.append(Paragraph("Step by Step", h2))

    story.append(Paragraph("<b>Stage 1 (the only manual setup):</b>", body_bold))
    for i, s in enumerate([
        "Open Stage-1-Technical-Intake.md",
        "Copy everything inside the code block",
        "Paste it into a new Claude conversation",
        "After the prompt, type or paste your invention description",
        "Send it",
    ], 1):
        story.append(Paragraph(f"{i}.  {s}", step_style))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Stage 2 (and every stage after):</b>", body_bold))
    for i, s in enumerate([
        "Claude produces a Stage 1 analysis, then a handoff block",
        "Copy everything from the COPY marker to the END marker",
        "Open a new Claude conversation",
        "Paste the handoff block and send it",
        "Repeat for Stages 3, 4, 5, and 6",
    ], 1):
        story.append(Paragraph(f"{i}.  {s}", step_style))
    story.append(Spacer(1, 6))

    story.append(Paragraph(
        "<b>That\u2019s it. One file to open. One copy-paste per stage. Six stages total.</b>",
        green_style))
    hr()

    # ===== WRITING A GOOD DESCRIPTION =====
    story.append(Paragraph("Writing a Good Invention Description", h1))
    story.append(Paragraph("The better your input, the better your analysis. Include:", body))
    for item in [
        "<b>What it does</b> \u2014 The problem it solves and for whom",
        "<b>How it works</b> \u2014 Architecture, algorithms, data flows, mechanical design, materials",
        "<b>What makes it different</b> \u2014 Why existing solutions don\u2019t do what yours does",
        "<b>What\u2019s built vs. conceptual</b> \u2014 Have you built a prototype, or is this still an idea?",
        "<b>Specific technologies</b> \u2014 AI models, sensors, manufacturing processes, materials, software",
    ]:
        story.append(Paragraph(f"\u2022  {item}", bullet))
    hr()

    # ===== EXECUTION LANES =====
    story.append(Paragraph("Execution Lanes", h1))
    story.append(Paragraph("You don\u2019t have to run all 6 stages. Useful shortcuts:", body))
    story.append(Spacer(1, 6))
    story.append(make_table(
        ["Lane", "Stages", "Use When"],
        [
            ["Full Analysis", "1 \u2192 2 \u2192 3 \u2192 4 \u2192 5 \u2192 6", "Complete patent feasibility assessment"],
            ["Quick Assessment", "1 \u2192 3 \u2192 5", "Fast check (skips deep prior art search)"],
            ["Prior Art Only", "1 \u2192 2", "Just want to know what\u2019s already out there"],
            ["Strategy Only", "1 \u2192 5", "Already know the landscape, need filing guidance"],
        ],
        col_widths=[1.5*inch, 2.2*inch, 2.8*inch]
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "For shortcut lanes, open the relevant Stage file directly and paste your previous "
        "stage outputs after it.", body))
    hr()

    # ===== WEB SEARCH =====
    story.append(Paragraph("Which Stages Need Web Search?", h1))
    story.append(make_table(
        ["Stage", "Web Search", "Why"],
        [
            ["1 \u2014 Technical Intake", "Not needed", "Pure analysis of your description"],
            ["2 \u2014 Prior Art Search", "Required", "Must search real patent databases, papers, products"],
            ["3 \u2014 Patentability", "Helpful", "Can look up recent case law and USPTO guidance"],
            ["4 \u2014 Deep Dive", "Helpful", "Can search domain-specific patent landscape"],
            ["5 \u2014 IP Strategy", "Not needed", "Synthesis and recommendations from prior stages"],
            ["6 \u2014 Final Report", "Not needed", "Assembles and synthesizes all previous outputs"],
        ],
        col_widths=[1.8*inch, 1*inch, 3.7*inch]
    ))
    hr()

    # ===== COST =====
    story.append(Paragraph("Cost", h1))
    story.append(Paragraph(
        "<b>No additional cost.</b> With a Claude Pro ($20/month), Claude Max, Claude Team, or "
        "Gemini Advanced ($20/month) subscription, running these prompts is included in your "
        "subscription. There are no per-run charges, no API fees, and no token costs. You\u2019re "
        "just using your chatbot.", green_style))
    hr()

    # ===== WHAT THE ANALYSIS COVERS =====
    story.append(Paragraph("What the Analysis Covers", h1))

    story.append(Paragraph("For All Inventions", h2))
    for item in [
        "Technical restatement in patent-ready language",
        "Prior art search across patents, papers, products, and open source",
        "Full patentability assessment (\u00a7101, \u00a7102, \u00a7103, \u00a7112)",
        "Common examiner concerns analysis for this technology area",
        "Filing landscape assessment (provisional vs. non-provisional, timing, costs)",
        "Claim direction recommendations",
        "Risk scoring (0\u2013100) for each statutory category",
        "Documentation checklist",
        "Plain-English summary anyone can understand",
    ]:
        story.append(Paragraph(f"\u2022  {item}", bullet))

    story.append(Paragraph("Special Depth for AI/ML Inventions", h2))
    for item in [
        "Patent zone classification (strong vs. red-flag categories)",
        "Alice/Mayo \u00a7101 deep analysis specific to AI",
        "Current USPTO AI guidance and Federal Circuit decisions",
        "AI claim framing strategy (system vs. method vs. CRM)",
        "Trade secret vs. patent boundary analysis for algorithms",
    ]:
        story.append(Paragraph(f"\u2022  {item}", bullet))

    story.append(Paragraph("Special Depth for 3D Printing Inventions", h2))
    for item in [
        "Design patent vs. utility patent analysis",
        "Category classification (geometry, process, material, software, post-processing)",
        "3D printing patent landscape search",
        "Design patent claiming strategy",
    ]:
        story.append(Paragraph(f"\u2022  {item}", bullet))
    hr()

    # ===== LEGAL DISCLAIMER =====
    story.append(Paragraph("Legal Disclaimer", h1))
    story.append(Paragraph(
        "This prompt system provides <b>AI-powered patent research support</b>, not legal advice. "
        "The author of this tool is not a lawyer. The AI systems that execute these prompts are not lawyers.", body))
    for item in [
        "Does <b>not</b> create an attorney-client relationship",
        "Does <b>not</b> constitute a formal patentability or freedom-to-operate opinion",
        "Should <b>not</b> be relied upon as a substitute for a registered patent attorney",
        "Is intended to help inventors understand the patent landscape before investing in formal legal work",
    ]:
        story.append(Paragraph(f"\u2022  {item}", bullet))
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Always consult a registered patent attorney before filing.</b>", body_bold))
    story.append(Spacer(1, 20))
    hr()
    story.append(Paragraph(
        "Developed and tested on Anthropic\u2019s Claude. Gemini Advanced is a supported alternative. "
        "Other LLMs lack the context window size required for later stages. Free-tier LLMs are "
        "not recommended.",
        footer_style))

    doc.build(story)
    print("PDF generated successfully!")

if __name__ == "__main__":
    build_pdf()
