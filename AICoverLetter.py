import streamlit as st
import google.generativeai as genai

st.title("Cover Letter Generator")

# Configure API
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash")

# Inputs
job_title = st.text_input("Job Title")
summary = st.text_area("Resume Summary")

# Button
if st.button("Generate Cover Letter"):
    prompt = f"Write a cover letter for {job_title} using these resume points:\n{summary}"
    response = model.generate_content(prompt)
    st.write(response.text)
