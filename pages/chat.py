import streamlit as st
import ollama
import pandas as pd
from authfuncs.authenticate import auth_check
from config import Config
from llmfuncs.base import get_models, stream_parse, send_chat
import authfuncs.authenticate as auth

st.set_page_config(
    page_title=Config.PAGE_TITLE,
    initial_sidebar_state=Config.SIDEBAR
)

with st.spinner("Loading..."):
    config = auth.config_auth()
    authenticator=auth.init_auth(config)
    auth.auth_check(authenticator)
    
auth.update_auth(config)

st.title(Config.PAGE_TITLE, anchor=False)

client = ollama.Client(host=Config.OLLAMA_HOST)
sys_prompt = Config.SYSTEM_PROMPT
selected_model=Config.DEFAULT_MODEL
model_list=get_models(client)

with st.sidebar:
    st.markdown("# Options")
    if model_list:
        selected_model = st.selectbox(
            "Choose an available model:", model_list
        )
    else:
        st.warning("No models available from ollama.")
    st.markdown("# Upload File")
    upload = st.file_uploader("Choose a file", type="csv,xlsx")
    st.markdown("# User")
    if st.session_state.get('authentication_status'):
        authenticator.logout()
    elif st.session_state.get('authentication_status') is False:
        st.error('Username/password is incorrect')
    elif st.session_state.get('authentication_status') is None:
        st.warning('Please enter your username and password')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Please enter a prompt..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Generating response..."):
        with st.chat_message("assistant"):
            response = send_chat(client, sys_prompt, prompt, selected_model)
            output = st.write_stream(stream_parse(response))
            st.session_state.messages.append(
                {"role": "assistant", "content": output}
            )