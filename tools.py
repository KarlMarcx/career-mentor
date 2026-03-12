import streamlit as st
from groq import Groq

# Load API key from Streamlit Secrets
client = Groq(api_key=st.secrets["GROQ_API_KEY"])


def ask_llm(prompt):

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


def career_advice(user_input):

    prompt = f"""
    You are a helpful career mentor for university students.

    Student question:
    {user_input}

    Give clear and practical career advice.
    """

    return ask_llm(prompt)


def skill_gap_analysis(user_input):

    prompt = f"""
    A student is asking about skills for a career.

    Question:
    {user_input}

    Provide:
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

    Suggest:
    - stronger wording
    - missing sections
    - improvements
    """

    return ask_llm(prompt)