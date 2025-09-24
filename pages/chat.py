import streamlit as st
import ollama as ol
import pandas as pd
from config import Config
from llmfuncs import base as lf
import authfuncs.authenticate as af
from menu import menu

st.set_page_config(
    page_icon=Config.PAGE_ICON,
    page_title=Config.CHAT_TITLE,
    initial_sidebar_state=Config.SIDEBAR
)

st.title=Config.CHAT_TITLE

af.auth_check()

authenticator = af.authenticate()

menu(authenticator)

sys_prompt = Config.SYSTEM_PROMPT

model_list = lf.get_models()
if model_list:
    selected_model = st.selectbox(
        "Choose an available model:", model_list
    )
    st.warning("Selecting a large model increases time to generate responses (e.g., gpt-oss:20b).")
else:
    st.warning("No models available from ollama.")

client = lf.create_client()

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.container():
    chat_container = st.container(border=True, height=400)
    for message in st.session_state.messages:
        with chat_container.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("Please enter a prompt..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with chat_container.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Generating response..."):
        with chat_container.chat_message("assistant"):
            response = lf.send_chat(client, sys_prompt, prompt, selected_model)
            output = chat_container.write_stream(lf.stream_parse(response))
            st.session_state.messages.append(
                {"role": "assistant", "content": output}
            )