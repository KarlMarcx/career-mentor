import streamlit as st
from groq import Groq

# Load API key from Streamlit Secrets
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def ask_llm(prompt):
    """Call Groq LLM with error handling."""
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # smaller, faster, suitable for this use case
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        # Log error and return user-friendly message
        print("LLM API Error:", e)
        return "Sorry, I'm having trouble answering that right now."

def career_advice(user_input):
    prompt = f"""
You are a helpful career mentor for university students.

Student question:
{user_input}

RULES:
- Only answer questions about careers, skills, or resumes.
- If the question is not related to careers, politely respond:
  "I'm here to give career advice. I can't answer that question."
- Give clear and practical career advice if the question is career-related.
"""
    return ask_llm(prompt)

def skill_gap_analysis(user_input):
    prompt = f"""
A student is asking about skills for a career.

Question:
{user_input}

RULES:
- Only answer questions about career-related skills or learning paths.
- If the question is not related to careers, politely respond:
  "I'm here to give career advice. I can't answer that question."
- Provide:
  - Important skills required
  - Tools or technologies to learn
  - Suggested learning path
"""
    return ask_llm(prompt)

def resume_review(user_input):
    prompt = f"""
Review this resume text and give improvement suggestions.

Resume:
{user_input}

RULES:
- Only provide suggestions for career-related content.
- If the input is not related to a resume or career, politely respond:
  "I'm here to give career advice. I can't answer that question."
- Suggest:
  - stronger wording
  - missing sections
  - improvements
"""
    return ask_llm(prompt)