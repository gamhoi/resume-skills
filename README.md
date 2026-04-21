# Resume Agent Skills Collection

Welcome to the **Resume Skills** repository! This is a collection of AI-powered workflows, prompt architectures, and local tooling designed to turn advanced LLMs (like Claude, Gemini, or ChatGPT via Cursor) into specialized career and resume assistants.

This repository uses the **Agent Skills** design pattern. By exposing specific `.md` files to your AI agent, you can override its generic behavior and grant it deep, specialized capabilities for distinct career-oriented tasks.

## 🚀 Available Skills

Currently, the repository hosts the following skill kits. Expect more to be added in the future!

### 1. Resume Generator (`skills/resume-generator`)
A local toolkit that translates unstructured base resumes into beautifully formatted, ATS-compliant PDFs and Word Documents (`.docx`). 
* **Improvement Mode:** The default mode for processing resumes. Uses a strict set of "Professional Content Improvement Rules" to automatically optimize content, emphasize action verbs, refine numerical metrics, and use HTML bolding (`<b>`) for hard capabilities.
* **JD Tailoring Mode:** An advanced, structured tailoring pipeline that parses JDs into 5 categories, scores your experience against requirements using confidence bands, discovers undocumented skills through targeted questions, and applies named reframing strategies — all governed by a strict *Translation, Not Fabrication* philosophy. See `jd-tailoring-guide.md` for full framework.

## 💻 Prerequisites

Many skills contain deterministic Python execution engines to construct formatted documents locally. Ensure you have Python installed, then install the global dependencies:

```bash
pip3 install -r skills/resume-generator/requirements.txt
```

## 🤖 Supported Agents & Frameworks

This entire repository is built to be ingested by advanced LLM agents. Here is how to load the skills into popular agent environments:

### Google Antigravity
Antigravity automatically discovers skills situated in your workspace. Simply ensure this repository is in your active workspace directory and you can directly prompt:
> *"Use the Resume Generator skill to tailor my resume for this JD."*

### Cursor IDE
Cursor needs a context pointer to adapt the rules. Open Cursor in this repository and either:
1. Copy the contents of your chosen skill (e.g., `skills/resume-generator/SKILL.md`) into your `.cursorrules` file.
2. Alternatively, just reference the file directly in the Chat interface: `@skills/resume-generator/SKILL.md generate a new resume from my text`.

### Claude Code (`claude`) / GitHub Copilot Agents
If you are running CLI agents like Claude Code or Copilot, start your session in the root workspace. Inform the agent of the capability you want to unlock upfront:
> *"Load the logic defined in `skills/resume-generator/SKILL.md`. I want to use the Improvement mode on my base resume."*

## 📁 Repository Structure

```text
.
├── LICENSE
├── README.md
├── AGENTS.md                             # Global instructions for autonomous AI agents
├── CLAUDE.md                             # Context rules automatically ingested by Claude Code
└── skills/
    ├── resume-generator/                 # [Skill] Unstructured Text -> ATS PDF/DOCX
    │   ├── SKILL.md                      # Core prompt constraints & JSON Schema
    │   ├── jd-tailoring-guide.md          # Detailed JD Tailoring strategies & frameworks
    │   ├── requirements.txt              
    │   └── scripts/                      # Local python execution engines
    └── [Future Skills...]                # E.g., Cover Letter Generator, Interview Prep
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
