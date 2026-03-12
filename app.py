import streamlit as st
from tools import career_advice, skill_gap_analysis, resume_review

st.set_page_config(page_title="CareerMentor AI")

st.title("🎓 CareerMentor AI")
st.write("An Agentic AI Career Advisor for Students")

# Chat input
user_input = st.chat_input("Ask about careers, skills, or resumes")


# Agent Router
def agent_router(query):

    query = query.lower()

    if "resume" in query:
        return resume_review(query)

    elif "skill" in query or "learn" in query:
        return skill_gap_analysis(query)

    else:
        return career_advice(query)


# Chat interaction
if user_input:

    with st.chat_message("user"):
        st.write(user_input)

    response = agent_router(user_input)

    with st.chat_message("assistant"):
        st.write(response)