import os
import streamlit as st
import google.generativeai as genai

# API Key from environment
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    st.error("API Key not found. Set API_KEY in environment variables.")
    st.stop()

genai.configure(api_key=API_KEY)

# Model
model = genai.GenerativeModel("models/gemini-1.5-flash")

# UI
st.title("🎯 AI Interview Preparation Bot")

category = st.selectbox(
    "Select Interview Type",
    ["HR Interview", "Python Interview", "AI/ML Interview"]
)

# Generate question
if st.button("Generate Question"):
    prompt = f"Generate one {category} interview question."
    response = model.generate_content(prompt)
    st.session_state.question = response.text

# Show question
if "question" in st.session_state:
    st.subheader("Question")
    st.write(st.session_state.question)

    answer = st.text_area("Your Answer")

    if st.button("Evaluate Answer"):
        feedback_prompt = f"""
        Question: {st.session_state.question}
        Answer: {answer}

        Give:
        - Score out of 10
        - Strengths
        - Weaknesses
        - Improvement tips
        """

        result = model.generate_content(feedback_prompt)
        st.subheader("AI Feedback")
        st.write(result.text)
