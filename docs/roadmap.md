# GenAI Projects Roadmap

This document lists the initial 10 projects implemented in this repository.
Each project lives in `projects/XX_*` and has its own README and code.

---

## 01 – Resume Intake & Candidate Intelligence Engine  
*(Used by HR tech companies)*

**Problem**  
Recruiters get resumes in every format → summaries are subjective.

**You build**  
- Input: raw resume (PDF/DOC)
- Output:
  - structured candidate profile (skills, experience, gaps)
  - role-fit score (from classifier or rule-based logic)
  - explanation in plain English (LLM)

**Why LLM**  
- Deep reasoning across experience
- Summarization with justification

**Why DL/NLP**  
- Skill classification
- Resume section detection

✅ This is NOT “text summarization”. This is a hiring intelligence system.

---

## 02 – Contract & Legal Clause Risk Analyzer  
*(LegalTech / Enterprise)*

**Problem**  
Legal teams miss risky clauses in long contracts.

**You build**  
- Input: contract PDF  
- Output:
  - risky clauses highlighted
  - risk score
  - explanation + suggestions

**Tech**  
- NLP models for clause classification  
- LLM for interpretation & rewrite  
- RAG only for clause references

✅ This is a compliance product, not a RAG demo.

---

## 03 – Analytics Copilot for Data Teams  
*(Very high-demand use case)*

**Problem**  
Business users can’t write SQL or interpret dashboards.

**You build**  
- Natural language → SQL  
- Query validation  
- Result explanation  
- Optional chart instructions  

**Why LLM**  
- Query reasoning  
- Explanation

**Why NLP**  
- Intent classification (trend vs comparison vs aggregation)

✅ This is what companies call an “AI Copilot”.

---

## 04 – Customer Support Intelligence System  
*(Not a simple “chatbot”)*

**Problem**  
Support teams drown in tickets.

**You build**  
- Input: ticket text  
- Output:
  - category
  - sentiment
  - auto-draft response
  - confidence score

**Tech**  
- DL model for classification  
- LLM for response drafting  
- Optional RAG only if a knowledge base exists

✅ This solves a real operations problem.

---

## 05 – Internal Policy Decision Assistant  
*(Enterprise-grade)*

**Problem**  
Employees ask policy questions; wrong answers = risk.

**You build**  
An assistant that:
- answers only if document evidence exists  
- refuses otherwise  
- cites policy text

**Key Point**  
- Precision > creativity  

✅ Very different from “chat with PDF”.

---

## 06 – Market Research & Report Generator  
*(Consulting / Strategy)*

**Problem**  
Analysts manually compile reports.

**You build**  
- Input: topic  
- Agents:
  - research
  - summarize
  - criticize
- Output: structured report

✅ Multi-agent used for a real workflow, not just a demo.

---

## 07 – Intelligent Email & Communication Assistant  
*(Productivity SaaS)*

**Problem**  
Professionals waste time rewriting emails.

**You build**  
- Tone detection (NLP)  
- Context understanding  
- Rewrite suggestions

✅ Combines NLP + LLM + product thinking.

---

## 08 – Domain-Specific Document Reviewer  
*(Finance / Healthcare / Aviation — pick one)*

**Problem**  
Documents are long, regulated, and high-risk.

**You build**  
- Domain-specific checks  
- Mandatory sections detection  
- Explanation of missing parts

✅ This shows domain adaptation, not generic AI.

---

## 09 – Incident Analysis & Post-Mortem Generator  
*(Engineering teams)*

**Problem**  
Post-mortems are badly written and inconsistent.

**You build**  
- Ingest logs + incident notes  
- Timeline extraction  
- Root cause reasoning  
- Improvement suggestions  

✅ Focus on hard reasoning, not RAG.

---

## 10 – Decision-Support System (Human-in-the-Loop)

**Problem**  
AI shouldn’t auto-decide in critical workflows.

**You build**  
- Suggestions  
- Confidence scores  
- Explicit approval flow (human in the loop)

✅ Demonstrates responsible GenAI system design.
