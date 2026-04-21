# JD Tailoring Guide

> Reference document for the Resume Generator skill's **JD Tailoring Mode**.
> This file contains detailed frameworks, scoring models, and strategies.
> The main workflow lives in `SKILL.md` — this file is referenced from there.

---

## 1. JD Parsing Framework

When the user provides a Job Description, analyze it systematically and extract the following **5 categories** before any rewriting:

### 1.1 Explicit Requirements

Split every requirement into **must-have** vs. **nice-to-have**:

```
MUST-HAVE (hard requirements):
- "5+ years of experience in C/C++"
- "Experience with real-time video processing"
- "Bachelor's degree in CS or related field"

NICE-TO-HAVE (preferred / bonus):
- "Experience with Kubernetes"
- "Familiarity with WebRTC"
- "AWS certifications a plus"
```

**How to classify:** Language like "required", "must have", "minimum" = must-have. Language like "preferred", "bonus", "nice to have", "ideally", "plus" = nice-to-have. If ambiguous, treat as must-have.

### 1.2 Technical & ATS Keywords (with Frequency Analysis)

Extract and categorize the keywords. **Crucially, track the frequency of each keyword** in the JD (e.g., if "C++" appears 4 times, note `C++ (4)`). High-frequency keywords are computationally more important to ATS algorithms and should be prioritized. Scan both the "Requirements" and the "Responsibilities/Duties" sections of the JD.

```
LANGUAGES:       C++ (4), Python (2), Go, TypeScript
FRAMEWORKS:      FFmpeg (3), WebRTC, gRPC, React
CLOUD/INFRA:     AWS (2), Kubernetes, Docker, Terraform
DOMAIN TERMS:    "real-time media processing" (2), "low-latency streaming", "edge computing"
WORKFLOWS:       "object detection", "algorithm optimization", "field deployments", "testing and validation"
SOFT SKILLS:     "Friendly" (1), "Localization" (1), "Security clearance" (1)
```

**Extract ALL Keywords from ALL Sections:** Modern ATS software uses exact string matching and does not distinguish between skills listed under Requirements versus Responsibilities. Do not ignore workflow descriptions (e.g., "collaborate with stakeholders", "prototyping"), soft skills (e.g., "Friendly"), or domain-specific nouns (e.g., "Security clearance", "Localization"). Extract them so they can be exact-matched.

### 1.3 Implicit Preferences

Read between the lines for signals the JD doesn't state explicitly:

```
IMPLICIT SIGNALS:
- "Fast-paced environment" → values self-starters, comfort with ambiguity
- "Cross-functional collaboration" → leadership/influence without authority
- "Scale from 0 to 1" → startup mentality, breadth over depth
- Emphasis on "ownership" → values end-to-end delivery, not just contribution
- Multiple mentions of "data-driven" → quantified metrics matter in bullets
```

### 1.4 Role Archetype

Classify the role to guide bullet emphasis:

| Archetype | Signals in JD | Bullet Emphasis |
|---|---|---|
| **IC Technical** | "design", "implement", "architect", "debug" | Technical depth, system design, performance metrics |
| **People Leadership** | "manage", "mentor", "hire", "grow the team" | Team size, hiring, mentorship, org impact |
| **Cross-Functional** | "coordinate", "stakeholders", "roadmap", "align" | Cross-team projects, stakeholder management, delivery metrics |

Most roles blend archetypes. Identify the **primary** (drives bullet selection) and **secondary** (supports it).

### 1.5 Terminology Map

Map the JD's preferred phrasing to common synonyms the user's resume might use. This drives the Keyword Alignment reframing strategy:

```
TERMINOLOGY MAP:
JD says                    → User's resume might say
"CI/CD pipelines"          → "automated build/deploy", "DevOps", "Jenkins pipelines"
"distributed systems"      → "microservices", "scalable architecture"
"observability"            → "monitoring", "logging", "Prometheus/Grafana"
"event-driven architecture"→ "message queues", "Kafka", "pub/sub"
"IaC (Infrastructure as Code)" → "Terraform", "CloudFormation", "Ansible"
```

---

## 2. Confidence Scoring Model

For each JD requirement (from Section 1.1), evaluate how well the user's existing experience matches. Use these confidence bands as a **mental model** — not a calculator:

| Band | Confidence | Meaning | Action |
|---|---|---|---|
| **DIRECT** | 90-100% | User has exact or near-exact experience | Use with confidence. Bold the keyword. |
| **TRANSFERABLE** | 75-89% | Same capability, different context or terminology | Reframe using Terminology Map (Section 4.1). |
| **ADJACENT** | 60-74% | Related experience that needs reframing to connect | Apply a reframing strategy (Section 4). Note in report. |
| **WEAK** | 45-59% | Stretch match; thin connection | Use only if no better option. Flag in report. |
| **GAP** | <45% | No meaningful match in user's experience | Ask user (Section 3). If still unmatched, flag as gap — do NOT fabricate. |

### Scoring Criteria (Weighted)

When assessing a match, consider these dimensions:

- **Direct Match (40%)** — Same keywords, domain, technology, outcome type, scale
- **Transferable Skills (30%)** — Same capability in different context, different stack but same problem class
- **Adjacent Experience (20%)** — Touched on the skill as secondary responsibility, used related tools
- **Impact Alignment (10%)** — Achievement type matches what the role values (metrics vs. collaboration vs. innovation)

### How to Apply

1. List every must-have and nice-to-have requirement from the JD parse
2. For each, find the user's **best matching** experience (bullet, role, or skill)
3. Classify into a confidence band
4. For GAP and WEAK: proceed to Gap Discovery (Section 3)
5. For ADJACENT and TRANSFERABLE: proceed to Content Reframing (Section 4)
6. For DIRECT: use as-is with keyword bolding

---

## 3. Gap Discovery Patterns

When confidence scoring reveals **GAP** (<45%) or **WEAK** (45-59%) matches, ask the user before giving up. Users often have relevant experience they didn't include in their resume.

### When to Ask

- Ask about **GAP and WEAK** matches for both mandatory requirements and nice-to-haves.
- Try to discover and improve the matching degree as much as possible for all missing keywords.
- Ask specific, direct questions. Do not suggest adding an "Interests" block to stuff keywords if there's no actual experience. Always base off the truth.

### Question Templates

**Technical Skill Gap:**
```
"The JD requires {SKILL}. Your resume doesn't mention it directly.
Have you worked with {SKILL} or anything closely related — even in
side projects, learning, or a supporting role?"
```

**Domain Experience Gap:**
```
"The role emphasizes {DOMAIN_AREA}. Have you had any exposure to
this area that isn't reflected in your current resume?"
```

**Soft Skill / Capability Gap:**
```
"The JD values {CAPABILITY} (e.g., 'cross-functional leadership').
Can you think of specific situations where you demonstrated this,
even informally?"
```

### How to Handle Responses

| User Response | Action |
|---|---|
| **Yes, with details** | Integrate into the JSON as a new bullet. Re-score to TRANSFERABLE or higher. |
| **Yes, but vague** | Ask one follow-up: _"Can you be more specific — what did you build/do, and what was the impact?"_ |
| **Tangentially related** | Assess if it's strong enough for ADJACENT (60%+). If yes, reframe. If no, flag as gap. |
| **No** | Accept the gap. Note in Tailoring Report. Suggest addressing in cover letter. |

### Key Principles

- **Keep it brief.** This is 2-5 minutes, not a 15-minute interview.
- **Ask, don't lead.** Let the user share naturally — don't suggest fake experience.
- **Capture immediately.** If the user shares something useful, draft a bullet on the spot and confirm.
- **Move on gracefully.** After one follow-up with no result, accept the gap and proceed.

---

## 4. Content Reframing Strategies

When a match is TRANSFERABLE (75-89%) or ADJACENT (60-74%), apply one of these four strategies to bridge the language gap between the user's experience and the JD's terminology. **All reframing must be truthful** — same facts, better framing.

### 4.1 Keyword Alignment

**When to use:** Good match, but the user's resume uses different terminology than the JD.

**Method:** Preserve meaning exactly, swap terminology to match the JD using the Terminology Map.

```
Before: "Set up automated build pipelines using Jenkins and Docker"
After:  "Implemented CI/CD pipelines using Jenkins and Docker for automated build and deployment"
Reason: JD uses "CI/CD pipelines" — same work, JD's preferred term.
```

```
Before: "Built monitoring dashboards with Prometheus and Grafana"
After:  "Delivered end-to-end observability leveraging Prometheus and Grafana"
Reason: JD uses "observability" — more precise term for the same capability.
```

### 4.2 Emphasis Shift

**When to use:** The facts match, but the JD values a different aspect (business outcome vs. technical method, or vice versa).

**Method:** Rearrange the same bullet to lead with what the JD values most.

```
Before: "Designed statistical experiments for quality testing, saving $3M in recall costs"
After:  "Prevented $3M in potential recall costs through predictive quality detection
         using statistical modeling"
Reason: JD emphasizes business impact → lead with the outcome.
```

```
Before: "Led team of 5 engineers to deliver the auth service"
After:  "Architected and delivered a high-availability authentication service with
         a team of 5 engineers"
Reason: JD is an IC technical role → lead with the technical contribution.
```

### 4.3 Abstraction Level

**When to use:** The JD is more or less technical than the user's bullet.

**Method:** Adjust specificity up or down to match the JD's tone.

```
Generalizing (JD is language-agnostic):
Before: "Built MATLAB-based automated evaluation system"
After:  "Developed automated evaluation system for production quality metrics"

Specializing (JD wants technical depth):
Before: "Built automated evaluation system"
After:  "Engineered automated evaluation pipeline (Python, scikit-learn) with
         CI/CD integration"
```

### 4.4 Scale Emphasis

**When to use:** The user has the experience, but the JD emphasizes a specific dimension of scale (team size, system scale, business impact, geographic reach).

**Method:** Highlight the dimension of scale the JD cares about.

```
Before: "Managed project with 3 partner teams"
After:  "Led cross-functional initiative coordinating 3 organizational units across
         engineering, product, and QA"
Reason: JD emphasizes cross-org complexity → expand on the collaboration dimension.
```

```
Before: "Optimized video processing pipeline"
After:  "Optimized video processing pipeline sustaining 50K concurrent streams with
         sub-200ms latency"
Reason: JD emphasizes hyperscale → add the scale metrics.
```

### 4.5 Exact Education & Metadata Matching

**When to use:** Mapping degrees, certifications, or clearances to the JD.

**Method:** Inspect the JD's explicit requirements (e.g., "Degree in Computer Science") and ensure the exact phrase is spelled out in the output JSON (e.g., write "Computer Science" rather than abbreviating to "CS"), provided the user actually possesses it.

### Reframing Constraints

> **CRITICAL:** All reframing is governed by the **"Translation, Not Fabrication"** principle from SKILL.md:
> - Every technical keyword in the reframed output must be traceable to the user's actual experience
> - Never inflate seniority, scale, or scope beyond what's truthful
> - When in doubt, keep the original phrasing

---

## 5. Tailoring Report Template

After completing the tailored JSON and **before** generating the PDF, present this report to the user for review:

```
═══════════════════════════════════════════════════════════
  TAILORING REPORT — {Role} at {Company}
═══════════════════════════════════════════════════════════

JD COVERAGE SUMMARY:
  ✅ Direct matches:       X requirements
  🔄 Transferable:         X requirements
  🔀 Adjacent (reframed):  X requirements
  ⚠️  Gaps (unaddressed):   X requirements
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Overall coverage:        XX%

REFRAMINGS APPLIED:
  1. "{original bullet}" →
     "{reframed bullet}"
     Strategy: {Keyword Alignment | Emphasis Shift | Abstraction Level | Scale Emphasis}

  2. ...

GAPS IDENTIFIED:
  1. {JD Requirement}: No matching experience found.
     → Recommendation: Address in cover letter / emphasize learning ability.

  2. ...

INTERVIEW PREP TIPS:
  • Be ready to discuss: {key experience areas that were reframed}
  • Expect questions about: {gap areas}
  • Strong talking points: {direct matches with impressive metrics}

═══════════════════════════════════════════════════════════
```

### Report Guidelines

- Present as a **chat message** (not a separate file) — keeps the flow simple
- The user reviews and confirms before you proceed to PDF generation
- If the user wants changes based on the report, revise the JSON and re-report
- Keep the report concise — 20-30 lines max, not a multi-page document
