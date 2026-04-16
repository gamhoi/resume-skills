# Claude Context

Welcome to the Anthropic Agent Skills repository! 

If you are an agent navigating this repository on behalf of a user, you instantly have access to the skillsets located in the `skills/` directory.

## Core Capabilities
Currently, this workspace contains the **Resume Generator** skill (`skills/resume-generator/SKILL.md`).

Whenever the user asks you to:
- Generate a resume
- Tailor a resume to a JD
- Improve a resume

You must strictly obey the prompt constraints, JSON schemas, ethical tailoring boundaries, and python script execution logic defined exclusively inside `skills/resume-generator/SKILL.md`.

## Execution
The generator operates via local python scripts. Ensure you are running python commands from the root directory but targeting the scripts within the `skills/` folder.

Example:
`python3 skills/resume-generator/scripts/generate_resume.py <input.json> <output.pdf>`
