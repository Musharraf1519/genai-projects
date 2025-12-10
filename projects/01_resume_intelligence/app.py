# app.py
# Project 01: Resume Intake & Candidate Intelligence Engine


import streamlit as st
import pdfplumber
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("Hiring Intelligence System.")

# These are *UploadedFile* objects, not paths
resume_file = st.file_uploader("Upload your Resume", type=["pdf"])
jd_file = st.file_uploader("Upload JD skills file (text)", type=["txt"])


# Extract Text From PDF
def extract_text(uploaded_pdf) -> str:
    """
    Extracts text from an uploaded PDF file (Streamlit UploadedFile).
    Returns a single string with all pages concatenated.
    """
    if uploaded_pdf is None:
        return ""

    try:
        with pdfplumber.open(uploaded_pdf) as pdf:
            if not pdf.pages:
                return ""

            all_text = []
            for page in pdf.pages:
                page_text = page.extract_text() or ""
                all_text.append(page_text)

            return "\n".join(all_text).strip()

    except FileNotFoundError:
        st.error("Error: The uploaded PDF file was not found.")
        return ""
    except Exception as e:
        st.error(f"An error occurred while reading the PDF: {e}")
        return ""


# Splitting The Extracted Text into Sections
def split_into_sections(text: str) -> dict:
    SECTION_KEYWORDS = {
        "skills": ["skills", "technical skills"],
        "experience": ["experience", "work experience", "professional experience"],
        "education": ["education", "academic background"]
    }
    sections = {name: [] for name in SECTION_KEYWORDS.keys()}

    current_section = None

    for line in text.splitlines():
        stripped = line.strip()
        lower = stripped.lower()

        found_new_section = False
        for section_name, keywords in SECTION_KEYWORDS.items():
            if any(kw in lower for kw in keywords):
                current_section = section_name
                found_new_section = True
                break

        if found_new_section:
            continue

        if current_section is not None and stripped:
            sections[current_section].append(stripped)

    # Join lists of lines into single strings
    return {name: "\n".join(lines).strip() for name, lines in sections.items()}


# Loading Skills From JD (from an UploadedFile)
def load_skill_list(uploaded_txt) -> list[str]:
    """
    Reads a text file uploaded via Streamlit and returns a list of skills (one per line).
    """
    if uploaded_txt is None:
        return []

    content = uploaded_txt.read().decode("utf-8", errors="ignore")
    skills = []
    for line in content.splitlines():
        s = line.strip().lower()
        if s:
            skills.append(s)

    return skills


# Extracting skills from Text
def extract_skills(text: str, known_skills: list[str]) -> list[str]:
    text_lower = text.lower()
    found = []
    for skill in known_skills:
        if skill in text_lower:
            found.append(skill)
    return sorted(set(found))


# Extract the Name (first non-empty line)
def extract_name(text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped
    return ""


# Building Candidate Profile
def build_candidate_profile(resume_text: str, sections: dict, skills_found: list[str]) -> dict:
    name = extract_name(resume_text)
    experience_text = sections.get("experience", "")
    education_text = sections.get("education", "")

    profile = {
        "name": name,
        "skills": skills_found,
        "experience_text": experience_text,
        "education_text": education_text
    }
    return profile


# Calculate Fitness of Profile
def compute_role_fit(candidate_skills: list[str], jd_skills: list[str]) -> dict:
    cand_set = set(s.lower() for s in candidate_skills)
    jd_set = set(s.lower() for s in jd_skills)

    matched = sorted(cand_set & jd_set)           # Intersection
    missing = sorted(jd_set - cand_set)           # In JD but not in candidate
    extra = sorted(cand_set - jd_set)             # In candidate but not in JD

    if len(jd_set) == 0:
        score = 0.0
    else:
        coverage = len(matched) / len(jd_set)
        score = round(coverage * 100, 1)

    if score >= 80:
        level = "Strong fit"
    elif score >= 50:
        level = "Partial fit"
    else:
        level = "Weak fit"

    return {
        "score": score,
        "level": level,
        "matched_skills": matched,
        "missing_skills": missing,
        "extra_skills": extra
    }


# Build a custom Prompt
def build_explanation_prompt(profile: dict, fit_result: dict, jd_skills: list[str]) -> str:
    return f"""
You are an HR assistant evaluating a candidate for a Data Engineer role.

Job description key skills:
{jd_skills}

Candidate name: {profile.get("name", "")}

Candidate skills:
{profile.get("skills", [])}

Matched skills:
{fit_result.get("matched_skills", [])}

Missing skills:
{fit_result.get("missing_skills", [])}

Extra (nice-to-have) skills:
{fit_result.get("extra_skills", [])}

Role-fit score: {fit_result.get("score", 0)} ({fit_result.get("level", "")})

Write:
1. A 2–3 line summary of the candidate fit.
2. 3 bullet points for strengths (skills or experience).
3. 3 bullet points for gaps or risks.
4. 3 bullet points with concrete recommendations to improve fit.

Be concise and objective.
"""


# Generate Explanation from LLMs (OpenAI)
def generate_fit_explanation(profile: dict, fit_result: dict, jd_skills: list[str]) -> str:
    prompt = build_explanation_prompt(profile, fit_result, jd_skills)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",   # or gpt-4o-mini / any chat model you have
        messages=[
            {"role": "system", "content": "You are a precise HR assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=400,
    )

    return response.choices[0].message.content.strip()


# Creating a Single Pipeline
def analyze_resume(uploaded_pdf, uploaded_jd_file) -> dict:
    # 1) PDF → text
    resume_text = extract_text(uploaded_pdf)
    if not resume_text:
        return {"error": "No text could be extracted from the resume PDF."}

    # 2) Load JD skills (text file → list of skills)
    jd_skills = load_skill_list(uploaded_jd_file)
    if not jd_skills:
        return {"error": "No skills found in the JD skills file."}

    # 3) Text → sections
    sections = split_into_sections(resume_text)

    # 4) Sections/Resume → skills
    skills_text = sections.get("skills", "") or resume_text
    skills_found = extract_skills(skills_text, jd_skills)

    # 5) Build basic profile
    profile = build_candidate_profile(resume_text, sections, skills_found)

    # 6) Compute role-fit
    fit_result = compute_role_fit(skills_found, jd_skills)

    # 7) Generate explanation (LLM)
    explanation = generate_fit_explanation(profile, fit_result, jd_skills)

    # 8) Return everything as one structured result
    return {
        "profile": profile,
        "role_fit": fit_result,
        "explanation": explanation
    }


# Streamlit UI logic
if st.button("Analyze Resume"):
    if resume_file is None or jd_file is None:
        st.error("Please upload both a resume PDF and a JD skills text file before analyzing.")
    else:
        result = analyze_resume(resume_file, jd_file)
        st.write(result)
