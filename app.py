import streamlit as st
from openai import OpenAI
import os

st.set_page_config(
    page_title="My Personal AI Agent",
    page_icon="🤖"
)

st.title("🤖 My Personal AI Agent")
st.write("Ask me anything.")

api_key = os.environ.get("OPENAI_API_KEY")

if not api_key:
    st.error("OpenAI API key is not configured.")
    st.stop()

client = OpenAI(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("What do you want me to do?")

if prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    answer = response.output_text

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    with st.chat_message("assistant"):
        st.write(answer)
