# app.py

import streamlit as st
from groq_client import ask_groq
from prompts import QA_PROMPT, EXPLAIN_PROMPT, SUMMARIZE_PROMPT

st.set_page_config(page_title="EduAssist — School Learning Chatbot", page_icon="📚", layout="centered")

st.title("📘 EduAssist — School Learning Chatbot")
st.write("Learn interactively using Groq LLM (GPT OSS 20B).")

# --- Mode Selection ---
mode = st.radio("Select mode:", ["Q&A", "Explain", "Summarize"])

user_input = st.text_area("Enter your question or text:")

if st.button("Ask"):
    if not user_input.strip():
        st.warning("Please enter a question or text.")
    else:
        with st.spinner("Thinking..."):
            try:
                if mode == "Q&A":
                    prompt = QA_PROMPT.format(question=user_input)
                elif mode == "Explain":
                    prompt = EXPLAIN_PROMPT.format(topic=user_input)
                else:
                    prompt = SUMMARIZE_PROMPT.format(text=user_input)

                result = ask_groq(prompt)
                st.success("Response:")
                st.write(result)

            except Exception as e:
                st.error(f"Error: {e}")
