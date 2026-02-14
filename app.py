{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
import google.generativeai as genai\
\
# Securely fetch your API Key from Streamlit Secrets\
api_key = st.secrets["GOOGLE_API_KEY"]\
genai.configure(api_key=api_key)\
\
st.title("My Gemini AI App")\
\
user_input = st.text_input("Ask me anything:")\
if st.button("Generate"):\
    model = genai.GenerativeModel('gemini-1.5-flash')\
    response = model.generate_content(user_input)\
    st.write(response.text)}