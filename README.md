# Story Writer Agent 🎬✍️

[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Google ADK](https://img.shields.io/badge/Framework-Google%20ADK-orange)](https://developers.google.com/)

> **Story Writer Agent** is a production-oriented, multi‑agent story generation framework built with **Google ADK**.  
> It combines a Director, Genre-specific Generators, and a Critic that iteratively refines drafts until they meet quality requirements.

---

## Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
- [Supported Genres](#supported-genres)
- [Project Structure](#project-structure)
- [Quickstart](#quickstart)
- [Development & Testing](#development--testing)
- [Extending the System](#extending-the-system)
- [Examples](#examples)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)
- [Assets & Demo](#assets--demo)

---

## Overview

The Story Writer Agent implements a **Hollywood-style creative pipeline**:
- **Director Agent**: orchestrates user requests, routes to appropriate genre generators, and handles high-level validation.
- **Generator Agents**: each genre (Romance, Fantasy, Sci‑Fi, etc.) has a focused generator that drafts story content.
- **Critic Agent**: evaluates drafts against configurable quality checks (coherence, pacing, character consistency, tone). If the draft fails, it returns structured feedback to the generator — triggering an improvement loop.

This pattern produces consistent, high-quality narrative output and is easy to extend with new genres and evaluation rules.

---

## Architecture

```
User Prompt
   │
   ▼
Director Agent (router, validation)
   │
   ▼
Genre Classifier → selects a Generator Agent
   │
   ▼
Generator Agent (draft)
   │
   ▼
Critic Agent (evaluate & score)
   ├── PASS → Final Story
   └── FAIL → Feedback → Generator revises (loop)
```

Key properties:
- **Modular** — each sub-agent is a separate Python package.
- **Iterative** — critic-guided improvement loop ensures quality.
- **Configurable** — evaluation criteria, stop conditions, and prompt templates are pluggable.

---

## Supported Genres

- Romantic  
- Adventure  
- Drama  
- Fantasy  
- Historical  
- Horror  
- Inspiration  
- Mystery  
- Sci‑Fi  
- Thriller

Each genre lives in its own package under `story_writer_agent/sub_agents/`, implemented as a drop-in generator.

---

## Project Structure

```
# 📂 Project Structure

story_writer_agent/
│
├── story_writer_agent/
│   │
│   ├── agent.py                    # Main Director agent
│   ├── __init__.py
│   │
│   ├── tools/                      # Shared utilities used by agents
│   │   ├── base_instruction.py     # Base prompt instructions
│   │   ├── critic.py               # Critic agent logic for story evaluation
│   │   ├── genre_classifier.py     # Detects story genre from user prompt
│   │   └── __init__.py
│   │
│   ├── sub_agents/                 # Genre-specific story generator agents
│   │   │
│   │   ├── Romantic/
│   │   │   ├── agent.py
│   │   │   └── __init__.py
│   │   │
│   │   ├── adventure/
│   │   │   ├── agent.py
│   │   │   └── __init__.py
│   │   │
│   │   ├── drama/
│   │   │   ├── agent.py
│   │   │   └── __init__.py
│   │   │
│   │   ├── fantasy/
│   │   │   ├── agent.py
│   │   │   └── __init__.py
│   │   │
│   │   ├── historical/
│   │   │   ├── agent.py
│   │   │   └── __init__.py
│   │   │
│   │   ├── horror/
│   │   │   ├── agent.py
│   │   │   └── __init__.py
│   │   │
│   │   ├── inspiration/
│   │   │   ├── agent.py
│   │   │   └── __init__.py
│   │   │
│   │   ├── mystery/
│   │   │   ├── agent.py
│   │   │   └── __init__.py
│   │   │
│   │   ├── scifi/
│   │   │   ├── agent.py
│   │   │   └── __init__.py
│   │   │
│   │   └── thriller/
│   │       ├── agent.py
│   │       └── __init__.py
│   │                    
├── config.py                       # Central configuration & constants
├── requirements.txt                # Python dependencies
├── .env                            # Environment variables (not checked in)
├── .gitignore
└── README.md
```

> **Note:** Every sub-agent folder contains `agent.py` and `__init__.py` to make it an importable package.

---

## Quickstart

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/story_writer_agent.git
cd story_writer_agent
```

### 2. Create and activate a virtual environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
# If you don't have requirements.txt
pip install google-adk
```

### 4. Add environment variables
Create a `.env` file (example):
```
GOOGLE_API_KEY=your_api_key_here
ADK_DEV=true
```

> Keep secrets out of version control. Add `.env` to `.gitignore`.

### 5. Start the ADK dev UI
```bash
adk dev
# then open http://localhost:8000/dev-ui and select "story_writer_agent"
```

---

## Development & Testing

- Run the Director locally via ADK dev UI for interactive testing.
- Unit test strategy:
  - Test genre classification independently.
  - Test critic scoring logic with synthetic drafts.
  - Mock LLM responses when running generator tests to avoid API usage.
- Linting & formatting:
  ```bash
  black .
  flake8
  ```

---

## Extending the System

### Add a new genre
1. Create a new directory under `story_writer_agent/sub_agents/`, e.g. `comedy/`.
2. Add `agent.py` that exposes the generator interface.
3. Add `__init__.py` to make it a package.
4. Register the genre in the Director or ensure the `genre_classifier` returns the new genre key.

### Customize critic checks
- Update `story_writer_agent/tools/critic.py`:
  - Add new scoring heuristics (consistency, trope checks, diversity).
  - Add configurable thresholds in `config.py`.

---

## Examples

**Prompt**
```
Write a short sci‑fi story about an engineer who rediscovers an ancient satellite.
```

**Flow**
1. Director routes prompt → Genre classifier yields “scifi”.
2. Sci‑Fi Generator drafts a 600‑word story.
3. Critic evaluates: finds weak character motivation → returns feedback.
4. Generator revises with improved motivation → final pass → output delivered.

---

## Roadmap

- Add **character memory** across stories for multi‑episode arcs.
- Implement **automated unit tests** for end‑to‑end runs using mock LLMs.
- Add **image generation** per scene and **audio narration** export.
- Create **CLI** for offline batch generation.

---

## Contributing

Contributions welcome. Suggested workflow:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feat/<your-feature>`.
3. Run tests and linters.
4. Open a pull request with a clear description and use cases.

---

## License

This project is released under the **MIT License**. See `LICENSE` for details.

---

## Author

**Praveen Ravva**  
AI Engineer — multi‑agent systems & generative AI

---

## Assets & Demo

- ADK Dev UI snapshot (development export): `stroy writer agent.html`. fileciteturn0file0
- Add screenshots and diagrams in `/docs` for better presentation (recommended).

---
