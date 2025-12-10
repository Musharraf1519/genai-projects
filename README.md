# GenAI Projects Monorepo

This repository contains a curated set of **Generative AI (GenAI) projects** focused on
**system-level engineering**, **applied NLP / ML**, and **real-world product use cases**.

Each project is:
- Designed to solve a concrete business problem
- Implemented as a standalone, runnable system
- Numbered to clearly show learning and complexity progression

This is **not a collection of demos**, but a portfolio of **production-style AI systems**.

---

## Projects

| # | Project |
|---|--------|
| 01 | Resume Intake & Candidate Intelligence Engine |
| 02 | Contract & Legal Clause Risk Analyzer |
| 03 | Analytics Copilot for Data Teams |
| 04 | Customer Support Intelligence System |
| 05 | Internal Policy Decision Assistant |
| 06 | Market Research & Report Generator |
| 07 | Intelligent Email & Communication Assistant |
| 08 | Domain-Specific Document Reviewer |
| 09 | Incident Analysis & Post-Mortem Generator |
| 10 | Decision-Support System (Human-in-the-Loop) |

Detailed descriptions and design notes are available in `docs/roadmap.md`.

---

## Repository Structure

genai-projects/<br>
├── common/ # Shared utilities (LLM clients, IO helpers, text utilities)<br>
├── projects/ # Numbered GenAI projects (01_* → 10_*)<br>
├── docs/ # Roadmap and architecture notes<br>
├── requirements.txt<br>
├── .env.example<br>
└── README.md <br>



- `common/` contains reusable components used across projects.
- Each folder inside `projects/` is a self-contained application with its own README.
- Environment secrets are **never committed**; see `.env.example`.

---

## Quickstart (Local Setup)

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows PowerShell
```

### 2. Install dependencies
```bash

pip install -r requirements.txt
```

### 3. Configure environment variables
Copy the template and add your API key:
```bash
cp .env.example .env
```
Edit .env and set:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```
### 4. Run Project 01 (example)
```bash
cd projects/01_resume_intelligence
streamlit run app.py
```

---

## About Me

I am an IT professional with approximately **5 years of industry experience**, primarily working as a **Data Analyst / Data Engineer**, with strong hands-on expertise in:

- Python and its data ecosystem  
- SQL for analytics and data transformation  
- Power BI for reporting and business insights  

Over the years, I have worked on turning raw data into actionable insights and
building analytical solutions used by business and technical stakeholders.

More recently, I have been expanding into **Generative AI and applied NLP**,
focusing on how LLMs can be integrated into real-world systems such as
decision-support tools, analytics copilots, and enterprise intelligence platforms.

This repository represents a structured transition from traditional data analytics
into **system-level GenAI engineering**, emphasizing practicality, explainability,
and responsible AI design.
