# Resume Generator

A local, AI-powered toolkit that translates unstructured base resumes into beautifully formatted, ATS-compliant PDFs and Word Documents (`.docx`). Designed specifically to be run locally, this generator ensures that your resume is styled cleanly, prioritizes metrics, and passes automated tracking screenings without resorting to keyword stuffing.

## Features

1. **Standard Generation:** Converts any base resume into a formal, two-page (or scaled) academic format using standard Serif fonts natively read by ATS systems.
2. **Improvement Mode:** Uses a strict set of "Professional Content Improvement Rules" to ensure bullet points prioritize Action Verbs, numerical metrics ("Show, Don't Tell"), standardized dates, and explicit HTML bolding (`<b>`) for hard capabilities.
3. **JD Tailoring Mode:** An ethical, advanced translation layer that reads a target Job Description (JD) and rephrases your historical experience to match demanded "Explicit Good Keywords." It employs a strict **Translation, Not Fabrication** philosophy to prevent hallucinated skills.
4. **Multi-Format Output:** Natively maps identical formatting parameters to both PDF (`reportlab`) and Word (`python-docx`).

## Prerequisites

You need Python 3 installed on your system.

Install all dependencies required for generation:

```bash
pip3 install -r requirements.txt
```

## Supported Agents & Frameworks

This skill relies on providing `SKILL.md` as context to an advanced LLM agent. Here is how to load it into popular agenting environments:

### Google Antigravity
Antigravity automatically discovers skills situated in your workspace. Simply ensure the `resume-generator` folder is in your active workspace directory and you can directly prompt:
> *"Use the Resume Generator skill to tailor my resume for this JD."*

### Cursor IDE
Cursor needs a context pointer to adapt the rules. Open Cursor and either:
1. Copy the contents of `skills/resume-generator/SKILL.md` into your `.cursorrules` file at the root of your workspace.
2. Alternatively, just reference the file directly in the Chat interface: `@skills/resume-generator/SKILL.md generate a new resume from my text`.

### Claude Code (`claude`) / GitHub Copilot Agents
If you are running CLI agents like Claude Code or Copilot, start your session in the root workspace where the `skills/` folder lives. Inform the agent of its capabilities upfront:
> *"Load the logic defined in `skills/resume-generator/SKILL.md`. I want to use the Improvement mode on my base resume."*

## Repository Structure

```text
.
├── LICENSE
├── README.md
├── AGENTS.md                             # Global instructions for autonomous AI agents
├── CLAUDE.md                             # Context rules automatically ingested by Claude Code
└── skills/
    └── resume-generator/
        ├── SKILL.md                      # The core LLM prompt constraint library
        ├── requirements.txt              # Python dependencies
        └── scripts/
            ├── generate_resume.py        # PDF compilation script
            └── generate_resume_docx.py   # DOCX compilation script
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
