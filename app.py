import streamlit as st
from tools import agent_router_dynamic

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

    # Prepare conversation history for routing
    history_text = "\n".join(
        [f"{m['role']}: {m['content']}" for m in st.session_state.messages]
    )

    # Get assistant response dynamically
    response = agent_router_dynamic(user_input, history_text)

    # Store assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.write(response)