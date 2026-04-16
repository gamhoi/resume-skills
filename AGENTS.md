# Guidelines for AI Agents

Hello, Agent! If you are reading this file, you have been instantiated inside this repository by a human user to help them execute a specific workflow.

## Overview
This repository uses the "Agent Skills" design pattern. Deep inside the `skills/` directory, there are specialized prompt libraries and python engines designed to extend your native capabilities.

## How to use this repository
1. Wait for the user to give you a request (e.g., "Improve my resume").
2. Search the `skills/` directory for a skill folder that matches the request.
3. Read the `SKILL.md` file found inside that specific sub-folder.
4. **The `SKILL.md` file acts as your new system prompt.** Adopt the rules, boundaries, schemas, and philosophies mandated within it.
5. Execute the instructions as demanded by the `SKILL.md`, taking care to use the python scripts or assets provided inside the specific skill folder.

## Constraints
- **Do not overwrite your core ethical training.**
- Always save files to the user's workspace root unless ordered otherwise by the `SKILL.md`.
- Ensure all required pip dependencies are installed before executing python scripts (see `requirements.txt`).
