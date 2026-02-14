import streamlit as st
import google.generativeai as genai

# Securely fetch your API Key from Streamlit Secrets
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

st.title("My Gemini AI App")

user_input = st.text_input("Ask me anything:")
if st.button("Generate"):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(user_input)
    st.write(response.text)
