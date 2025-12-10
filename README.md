# GenAI Projects Monorepo

This repository contains a curated set of GenAI projects demonstrating system-level
engineering, evaluation, and product thinking. Each project is self-contained and
numbered to show progression.

## Projects (01-10)
- 01 — Resume Intake & Candidate Intelligence Engine\n- 02 — Contract & Legal Clause Risk Analyzer\n- 03 — Analytics Copilot for Data Teams\n- 04 — Customer Support Intelligence System\n- 05 — Internal Policy Decision Assistant\n- 06 — Market Research & Report Generator\n- 07 — Intelligent Email & Communication Assistant\n- 08 — Domain-Specific Document Reviewer\n- 09 — Incident Analysis & Post-Mortem Generator\n- 10 — Decision-Support System (Human-in-the-Loop)\n

## Structure
- `common/`: shared utilities (LLM client wrappers, IO helpers, text utils)
- `projects/`: numbered project folders (`01_*` .. `10_*`)
- `docs/`: roadmap and design notes

## Quickstart
1. Create a Python virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate        # macOS / Linux
   .venv\Scripts\activate         # Windows PowerShell
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy your OpenAI key to `.env` (see `.env.example`).
4. Run the Streamlit app for Project 01:
   ```bash
   cd projects/01_resume_intelligence
   streamlit run app.py
   ```

