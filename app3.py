from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import os

# Load environment variables
load_dotenv()

# Configure the API key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Initialize the generative model and chat
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_response(query):
    try:
        response = chat.send_message(query, stream=True)
        return response
    except Exception as e:
        st.error(f"Error getting response: {e}")
        return []

# Streamlit app
st.title('Google Gemini Pro')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    response = get_response(prompt)
    response_text = ""
    with st.chat_message("assistant"):
        for chunk in response:
            response_text += chunk.text
            st.write(chunk.text)

    # Add response message to chat history
    st.session_state.messages.append({"role": "assistant", "content": response_text})
