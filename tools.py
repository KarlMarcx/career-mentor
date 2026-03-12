import streamlit as st
from tools import career_advice, skill_gap_analysis, resume_review, ask_llm

# ---------------------------
# Page Setup
# ---------------------------
st.set_page_config(page_title="CareerMentor AI")
st.title("🎓 CareerMentor AI")
st.write("An Agentic AI Career Advisor for Students")

# ---------------------------
# Initialize session state
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []  # store conversation history

# ---------------------------
# Chat Input
# ---------------------------
user_input = st.chat_input("Ask about careers, skills, or resumes")

if user_input:
    # Store and display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # ---------------------------
    # Agentic Tool Selector
    # ---------------------------
    def agent_router_dynamic(user_input, history):
        # Build a prompt to let the AI decide which tool to use
        tool_prompt = f"""
        You are a career mentor agent. Choose the appropriate tool for this user question:
        - Resume Review: if the user wants help with their resume.
        - Skill Gap Analysis: if the user asks about skills to learn or career growth.
        - Career Advice: for general career questions.

        Respond ONLY with the tool name exactly: "resume", "skills", or "career".

        Conversation so far:
        {history}
        User question: {user_input}
"""
        try:
            tool_choice = ask_llm(tool_prompt).strip().lower()
        except Exception:
            tool_choice = "career"  # fallback

        # Route to the correct function
        if "resume" in tool_choice:
            return resume_review(user_input)
        elif "skill" in tool_choice:
            return skill_gap_analysis(user_input)
        else:
            return career_advice(user_input)

    # ---------------------------
    # Prepare conversation history as text
    # ---------------------------
    history_text = "\n".join(
        [f"{m['role']}: {m['content']}" for m in st.session_state.messages]
    )

    # ---------------------------
    # Get assistant response
    # ---------------------------
    response = agent_router_dynamic(user_input, history_text)

    # Store assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})

    # ---------------------------
    # Display assistant response
    # ---------------------------
    for paragraph in response.split("\n\n"):
        if paragraph.strip():
            with st.chat_message("assistant"):
                st.write(paragraph)