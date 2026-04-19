---
name: "Resume Generator"
description: "Generates a clean, formal, ATS-compliant resume from an unstructured base resume. Operates by default in 'Improve' mode to aggressively rewrite content for maximum professional impact, and offers a 'Tailor' mode to intelligently match ATS algorithms against a specific Job Description (JD). Outputs natively to PDF (default) or MS Word (.docx)."
---

# Resume Generator Skill

Use this skill whenever a user asks to "generate a new resume", "build me a resume", "improve my resume", "tailor my resume" or similar requests involving translating a base resume into an optimized, ATS-friendly document. The skill operates in 2 distinct modes depending on the user's request:

1. **Improvement Mode:** The default mode for processing requests. Aggressively applies the Professional Content Improvement Rules to rewrite bullets, emphasize action verbs, standardize formatting, and natively bold prominent hard capabilities.
2. **JD Tailoring Mode:** Triggered by **"tailor my resume"** alongside a target Job Description. Translates the user's historical experience into the exact "Good" keywords demanded by the JD, deleting irrelevant noise.

**Output Format:** Output is always **PDF** by default. If the user explicitly requests Word format, you can output a **.docx**.

> **Note:** JD Tailoring Mode is a *superset* of Improvement Mode. When tailoring, ALL formatting rules from the Professional Content Optimization step (Keyword Bolding, Action Verbs, Metrics, etc.) are automatically applied in addition to the JD-specific translation logic.

## Prerequisites

Before running the generation scripts, ensure the following Python dependencies are installed:
```
pip3 install reportlab python-docx
```

## Workflow

1. **Information Extraction**:
   - Ask the user to provide their base resume if they haven't already.
   - The resume may come in any format (PDF, DOCX, TXT, or raw text pasted into chat). If the user provides a PDF or DOCX file, use an appropriate tool to extract its text content before proceeding.
   - Extract the information into the standardized JSON schema defined below. Do not try to rewrite or optimize yet; just map the raw text to the right structural fields (Contact, Summary, Experience, Projects, Education, Skills).

2. **Professional Content Optimization**:
   - As the core generation behavior, you must take the extracted JSON and rewrite its contents generating a *new, optimized JSON* output using these Professional Content Improvement Rules:
     - **Keyword Integration:** Ensure hard skills and important industry keywords are listed in a dedicated `SKILLS` section AND organically integrated into the bullet points under `WORK EXPERIENCE` to showcase how they were used.
     - **Keyword Bolding:** Wrap prominent hard skills, technologies, and crucial keywords within the `summary` and `experience` bullet points using standard HTML bold tags (e.g., `engineered using <b>Python</b> and <b>AWS</b>`). This creates scanning highlights.
     - **Show, Don't Tell (Metrics over Buzzwords):** Remove hollow buzzwords (e.g., "hard-working," "team player," "go-getter"). Rewrite bullet points using strong action verbs and quantifiable metrics (e.g., "Delivered X in Y timeframe, resulting in Z revenue growth").
     - **Action Verbs First:** Start every bullet point under `WORK EXPERIENCE` or `PROJECTS` with a strong action verb (use present tense if employed there currently, past tense otherwise).
     - **Number Formatting:** Write out numbers below 10 (e.g., "one", "two", "three") instead of digits, *unless* it refers to "10 years" or "15+ years".
     - **Date Formatting:** Never use leading zeroes for single-digit days or months (e.g., write "March 1, 2024", never "March 01, 2024").
     - **Abbreviations:** Avoid internal/lazy abbreviations (like etc., A/P, A/R). Always spell out industry terms precisely, followed by their acronym if matching typical job descriptions (e.g., Applicant Tracking System (ATS)).

3. **JD Tailoring Mode (If requested)**:
   - If the user provides a target Job Description (JD) and asks to "tailor" their resume, you will execute a highly advanced translation phase. **Note: All formatting/metric rules from the Professional Content Optimization step (Keyword Bolding, Action Verbs, Metrics) MUST still be applied during Tailoring!**
   - Intelligently parse the JD with a strict focus on extracting **Explicit "Good" Keywords** (defined as hard technical skills, domain-specific programming languages, frameworks, specialized tools, and precise industry terminology like "event-driven architecture" or "SIP/RTP").
   - **Ignore "Dumb" Keywords**: Do NOT blindly stuff generic nouns, basic soft skills, or universal corporate verbs (e.g., "team", "customer", "meetings", "troubleshooting", "participating") just to satisfy low-level keyword matchers. Maintain the high-impact "Show, Don't Tell" metric methodology.
   - **CORE PRINCIPLE — "Translation, Not Fabrication":**
     - Tailoring means **rephrasing existing experience** using the target JD's keywords to describe the same or similar work. It does **NOT** mean inventing skills or technologies the user never used.
     - **Allowed:** If the user's resume says "C++11", you may write "C++14/17" because these are closely related versions of the same language. If the user worked on "real-time media servers", you may rephrase that as "mission-critical communications software" if the JD uses that term.
     - **Forbidden:** If the user has no JavaScript experience anywhere in their resume, you MUST NOT add "JavaScript" just because the JD lists it. That is lying. Only match JD keywords that genuinely map to the user's actual experience.
     - **Rule of thumb:** Every technical keyword in the tailored output must be traceable back to something the user actually did in their original resume.
   - **Targeted Rewriting:**
     - Rewrite the `summary` to explicitly declare the targeted JD title and mirror the core technical mission of the opening, using only skills the user genuinely possesses.
     - Swap generic technical terms in the user's base resume for the exact phrasing/jargon used in the JD, when the underlying skill is the same or closely related.
     - Prune (delete) irrelevant technologies or bullet points to reduce noise, bringing the user's **legitimately matching** skills to the forefront of the bullet points and `SKILLS` section.
     - Ensure any overlapping "nice-to-have" technical skills from the JD are heavily emphasized — but only if the user's original resume demonstrates legitimate experience with them.

4. **JSON Schema**:
   - Map the extracted (and optionally improved) info into the precise JSON schema below. DO NOT change the keys; strictly adhere to this schema. Add a `projects` array if necessary.
   - The `summary` field MUST be an **array of strings** (bullet points), not a single string.
     ```json
     {
       "contact": {
         "name": "Jane Doe",
         "email": "jane@example.com",
         "phone": "(123) 456-7890",
         "linkedin": "linkedin.com/in/janedoe",
         "location": "City, State"
       },
       "summary": [
         "10+ years of professional experience...",
         "Specialized in backend APIs..."
       ],
       "experience": [
         {
           "title": "Software Engineer",
           "company": "Tech Corp",
           "dates": "Jan 2020 - Present",
           "location": "Remote",
           "bullets": ["Developed scalable...", "Led a project..."]
         }
       ],
       "projects": [
         {
           "name": "Open Source Tool",
           "dates": "May 2022",
           "description": "A tool that does X",
           "bullets": ["Implemented Y..."]
         }
       ],
       "education": [
         {
           "degree": "Bachelor of Science in Computer Science",
           "school": "University of Tech",
           "dates": "Sep 2015 - May 2019",
           "location": "City, State",
           "details": ["Minor in Math", "GPA: 3.8"]
         }
       ],
       "certifications": [
         {
           "name": "AWS Certified Solutions Architect – Associate",
           "date": "January 2026",
           "issuer": "Amazon Web Services (AWS)"
         }
       ],
       "skills": [
         {
           "category": "Languages",
           "items": ["Python", "JavaScript", "C++"]
         }
       ]
     }
     ```
   
5. **Execution**:
   - Write the finalized JSON to a file in the **user's workspace directory** (e.g., `<workspace>/resume_data.json`). Do NOT write it into the skill's own directory.
   - Execute the appropriate Python generation script to convert the JSON into the compiled format. Both scripts support native HTML `<b>` tags. Use `python3`.
   - Name the output file descriptively in the **user's workspace directory** (e.g., `<workspace>/Jason_Chen_Resume.pdf`).
   - **Default (PDF)**:
     - Command: `python3 <path_to_resume-generator>/scripts/generate_resume.py <path_to_input_json> <path_to_output>.pdf`
   - **If specifically requested (Word / .docx)**:
     - Command: `python3 <path_to_resume-generator>/scripts/generate_resume_docx.py <path_to_input_json> <path_to_output>.docx`

6. **Completion**:
   - Inform the user that the resume has been generated and provide the absolute path to the output file.
