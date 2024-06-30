from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import os

load_dotenv()   # take environment variables from .env.

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel("gemini-pro")

def get_response(query):
    response = model.generate_content(query)
    print(type(response))
    return response.text

# query = input("user : ")
# print("google-gemini : ", get_response(query))

st.title('Google Gemini Pro')
query = st.text_input("User : ", key="input")
if st.button("Generate Response"):
    st.write(get_response(query))