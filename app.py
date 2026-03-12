import streamlit as st
from tools import career_advice, skill_gap_analysis, resume_review

# ---------------------------
# Page Setup
# ---------------------------
st.set_page_config(page_title="CareerMentor AI")
st.title("🎓 CareerMentor AI")
st.write("An Agentic AI Career Advisor for Students")

# ---------------------------
# Chat Input
# ---------------------------
user_input = st.chat_input("Ask about careers, skills, or resumes")

# ---------------------------
# Agent Router
# ---------------------------
def agent_router(query):
    query = query.lower()
    if "resume" in query:
        return resume_review(query)
    elif "skill" in query or "learn" in query:
        return skill_gap_analysis(query)
    else:
        return career_advice(query)

# ---------------------------
# Chat Interaction
# ---------------------------
if user_input:
    # Display user's message
    with st.chat_message("user"):
        st.write(user_input)

    # Get assistant's response
    response = agent_router(user_input)

    # Handle multi-line or list responses neatly
    if isinstance(response, list):
        for part in response:
            with st.chat_message("assistant"):
                st.write(part)
    else:
        # Split by paragraphs to make long responses scroll naturally
        for paragraph in response.split("\n\n"):
            if paragraph.strip():  # skip empty lines
                with st.chat_message("assistant"):
                    st.write(paragraph)