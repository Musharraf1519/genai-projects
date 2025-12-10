# Architecture Notes

This document captures high-level architecture decisions for the `genai-projects` monorepo.
It is not meant to duplicate code or README files, but to explain **how the system is structured**
and **why** it is designed this way.

---

## 1. Repository Architecture

### 1.1 Monorepo Rationale

- All GenAI projects live in a **single repository**:
  - Easier to share common utilities (LLM client, IO helpers, text utilities)
  - Shows clear progression from basic to advanced systems
  - Mirrors how internal ML/AI platforms are often organized in companies

- Projects are numbered (`01_` to `10_`) to:
  - Indicate learning and complexity progression
  - Make it easy to reference projects in discussions and interviews

### 1.2 Directory Layout

- `common/`
  - Shared utilities used across projects
  - Examples:
    - `llm_client.py`: OpenAI client wrapper
    - `io_utils.py`: PDF/text extraction helpers
    - `text_utils.py`: basic text normalization/regex helpers

- `projects/`
  - Each subfolder is a **self-contained project**:
    - Own `README.md`
    - Own entrypoint (e.g., `app.py`)
    - Optional `sample_data/` for quick demo

- `docs/`
  - `roadmap.md`: list and description of all projects
  - `architecture_notes.md`: this file

- `.env` / `.env.example`
  - `.env.example` documents required environment variables (no secrets)
  - `.env` (local only) stores actual keys such as `OPENAI_API_KEY`

- `requirements.txt`
  - Central dependency file for the monorepo
  - Keeps setup simple: `pip install -r requirements.txt`

---

## 2. Project 01 – Resume Intake & Candidate Intelligence Engine

### 2.1 High-Level Flow

**Goal:** Turn a raw resume (PDF) + JD skill list (text file) into a structured profile and role-fit explanation.

**Main steps:**

1. **Input layer (Streamlit)**
   - Upload resume (`PDF`)
   - Upload JD skills (`.txt`, one skill per line)

2. **Resume parsing**
   - `extract_text(uploaded_pdf)`:
     - Uses `pdfplumber` to read all pages
     - Concatenates text into a single string

3. **Section detection**
   - `split_into_sections(text)`:
     - Simple rule-based splitting using section keywords:
       - `skills`, `experience`, `education`
     - Stores sections in a dict:
       - `{"skills": "...", "experience": "...", "education": "..."}`

4. **JD skills loading**
   - `load_skill_list(uploaded_txt)`:
     - Reads each line, normalizes to lowercase
     - Produces a list of skills expected from the JD

5. **Skill extraction from resume**
   - `extract_skills(text, known_skills)`:
     - Lowercases resume text
     - Checks if each JD skill appears as a substring
     - Returns unique, sorted list of matched skills

6. **Candidate profile construction**
   - `build_candidate_profile(resume_text, sections, skills_found)`:
     - Heuristic name extraction (first non-empty line)
     - Uses extracted sections for experience and education
     - Result: a structured Python `dict` profile

7. **Role-fit scoring**
   - `compute_role_fit(candidate_skills, jd_skills)`:
     - Computes intersection / differences between skill sets
     - Calculates coverage score: `|matched| / |jd_skills|`
     - Labels fit: `Strong / Partial / Weak`

8. **LLM explanation**
   - `build_explanation_prompt(...)`:
     - Builds a detailed prompt with:
       - JD skills
       - Candidate profile
       - Matched/missing/extra skills
       - Role-fit score + level
   - `generate_fit_explanation(...)`:
     - Calls OpenAI chat completion
     - Returns a plain-English explanation summarizing:
       - Fit
       - Strengths
       - Gaps
       - Recommendations

9. **Output (Streamlit)**
   - `analyze_resume(...)` returns a dict with:
     - `profile`
     - `role_fit`
     - `explanation`
   - UI currently uses `st.write(result)` (baseline version).

### 2.2 Design Choices (v1)

- **Simple, explicit pipeline**
  - Keeps each step testable and replaceable
  - Easier to extend later (e.g., swapping skill matcher with ML model)

- **Rule-based skill matching**
  - Fast to implement
  - Good enough for a baseline
  - Makes the scoring logic transparent

- **LLM only for explanation**
  - Deterministic parts (scoring, matching) done with Python
  - LLM used where natural language is valuable:
    - Summaries
    - Justifications
    - Recommendations

### 2.3 Known Limitations / Future Improvements

- Skill matching is substring-based (e.g., "sql" may match "nosql")
- JD is currently a simple skill list file, not a full free-text description
- Name extraction is heuristic and fragile
- No separate model for:
  - Seniority estimation
  - Domain tagging
  - Experience level scoring

These issues are acceptable for **v1** and will be addressed in future versions.

---

## 3. Conventions for Future Projects

- Each project:
  - Lives in its own folder under `projects/XX_*`
  - Has a `README.md` with:
    - Problem
    - Objective
    - Input / Output
    - Techniques

- Shared logic should move into `common/` once used by 2+ projects.

- Environment variables:
  - Always documented in `.env.example`
  - Never hard-coded in code
  - Never commit `.env` or secrets

- LLM usage:
  - Reserved for:
    - Natural language understanding / generation
    - Explanation, summarization, suggestion
  - Deterministic logic (scoring, validation, parsing) should be kept in Python, rules, or ML models where possible.
