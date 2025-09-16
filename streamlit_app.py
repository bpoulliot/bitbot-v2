import streamlit as st
import ollama
import os
import re
import json
import requests

st.title("BitBot")

OLLAMA_DEFAULT=os.getenv("OLLAMA_URL","http://127.0.0.1:11434")
DEFAULT_MODEL=os.getenv("OLLAMA_MODEL","llama3.1:8b")

# generate random response from following options
def response_generator():
    response = random.choice(
        [
            f"What's going on {st.session_state.name}?",
            "Hello meatbag!",
            "What can I help you with?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

# init models
if "model" not in st.session_state:
    st.session_state["model"] = ""

models = [model["name"] for model in ollama.list()["models"]]
st.session_state["model"] = st.selectbox("Choose your model", models)

# initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages=[]

# display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# react to user input
if prompt := st.chat_input("What's up?"):
    # display user message in container
    st.chat_message("user").markdown(prompt)
    # add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    st.session_state.messages.append({"role": "assistant", "content": response})

