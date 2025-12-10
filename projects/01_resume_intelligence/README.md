# 01 – Resume Intake & Candidate Intelligence Engine (v1)

## Problem
Recruiters receive resumes in multiple formats, and manual screening is subjective and inconsistent.

## What this version does (v1)
- Accepts resume PDFs
- Accepts a JD skill list (text file)
- Extracts resume text
- Builds a structured candidate profile
- Computes a rule-based role-fit score
- Generates a plain-English explanation using an LLM

## Tech Stack
- Python
- Streamlit
- pdfplumber
- OpenAI (LLM for explanation)
- Rule-based skill matching

## Notes
This is a **baseline implementation**.
Future versions will introduce:
- Automatic JD skill extraction
- ML/DL-based skill classification
- Improved fit scoring
- Stronger resume section detection
