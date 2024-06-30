from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

load_dotenv()   # take environment variables from .env.

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel("gemini-pro-vision")
model_text = genai.GenerativeModel("gemini-pro")

def get_response(image, query="Describe the image"):
    if image is None:
        response = model_text.generate_content(query)
        return response.text
    
    response = model.generate_content([query,image])
    return response.text


# Streamlit application
st.title('Google Gemini Pro')

image = st.file_uploader("Choose a file", type=["jpg","png","jpeg"])
query = st.text_input("User : ", key="input")

if image is not None:
    image = Image.open(image)
    st.image(image,caption="Uploaded image", use_column_width=True)


if st.button("Generate Response"):
    if image is not None:
        if(query == ""):
            st.write(get_response(image))
        else:
            st.write(get_response(image,query))
    else:
        st.write(get_response(image,query))