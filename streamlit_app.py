import streamlit as st
from langchain_openai.chat_models import ChatOpenAI

st.title("🦜🔗 Quickstart App")

# Access environment variables as if they came from the actual environment
openai_api_key = st.secrets["OPENAI_API_KEY"]


def generate_response(input_text):
    model = ChatOpenAI(
        model="gpt-3.5-turbo",  # <-- ADD this line
        temperature=0.7,
        api_key=openai_api_key,
    )
    try:
        response = model.invoke(input_text)
        st.info(response)
    except Exception as e:
        st.error(f"Error: {str(e)}")


with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )
    submitted = st.form_submit_button("Submit")
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")
    if submitted and openai_api_key.startswith("sk-"):
        generate_response(text)
