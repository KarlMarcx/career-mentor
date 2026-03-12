import streamlit as st
from groq import Groq

# Load API key from Streamlit Secrets
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ---------------------------
# Core LLM call with error handling
# ---------------------------
def ask_llm(prompt):
    """Call Groq LLM safely."""
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        print("LLM API Error:", e)
        return "Sorry, I'm having trouble answering that right now."

# ---------------------------
# Career Advice
# ---------------------------
def career_advice(user_input):
    prompt = f"""
You are a helpful career mentor for university students.

Student question:
{user_input}

RULES:
- Only answer questions about careers, skills, or resumes.
- If the question is not related to careers, respond exactly:
  "I'm here to give career advice. I can't answer that question."
- Give clear and practical career advice if the question is career-related.
"""
    return ask_llm(prompt)

# ---------------------------
# Skill Gap Analysis
# ---------------------------
def skill_gap_analysis(user_input):
    prompt = f"""
A student is asking about skills for a career.

Question:
{user_input}

RULES:
- Only answer questions about career-related skills or learning paths.
- If the question is not related to careers, respond exactly:
  "I'm here to give career advice. I can't answer that question."
- Provide:
  - Important skills required
  - Tools or technologies to learn
  - Suggested learning path
"""
    return ask_llm(prompt)

# ---------------------------
# Resume Review
# ---------------------------
def resume_review(user_input):
    prompt = f"""
Review this resume text and give improvement suggestions.

Resume:
{user_input}

RULES:
- Only provide suggestions for career-related content.
- If the input is not related to a resume or career, respond exactly:
  "I'm here to give career advice. I can't answer that question."
- Suggest:
  - stronger wording
  - missing sections
  - improvements
"""
    return ask_llm(prompt)

# ---------------------------
# Agentic Router (dynamic tool selection)
# ---------------------------
def agent_router_dynamic(user_input, history_text):
    """
    Let the AI decide which tool to use based on conversation history.
    """
    tool_prompt = f"""
You are a career mentor agent. Choose the appropriate tool for this user question:
- Resume Review: if the user wants help with their resume.
- Skill Gap Analysis: if the user asks about skills to learn or career growth.
- Career Advice: for general career questions.

Respond ONLY with the tool name exactly: "resume", "skills", or "career".

Conversation so far:
{history_text}

User question: {user_input}
"""
    try:
        tool_choice = ask_llm(tool_prompt).strip().lower()
    except Exception:
        tool_choice = "career"  # fallback

    if "resume" in tool_choice:
        return resume_review(user_input)
    elif "skill" in tool_choice:
        return skill_gap_analysis(user_input)
    else:
        return career_advice(user_input)