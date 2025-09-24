import streamlit as st
from authfuncs import authenticate as af
from menu import menu
from llmfuncs import base as lf
from config import Config

st.set_page_config(
    page_icon=Config.PAGE_ICON,
    page_title=Config.SETTINGS_TITLE,
    initial_sidebar_state=Config.SIDEBAR
)

st.title=Config.SETTINGS_TITLE

st.header("User Options", anchor=False, divider="red")

af.auth_check()

authenticator = af.authenticate()
config = af.config_auth()

menu(authenticator)

if st.session_state.get('authentication_status'):
    try:
        if authenticator.update_user_details(st.session_state.get('username')):
            st.success('Entries updated successfully')
            af.update_auth(config)
    except Exception as e:
        st.error(e)

if st.session_state.get('authentication_status'):
    try:
        if authenticator.reset_password(st.session_state.get('username')):
            st.success('Password modified successfully')
            af.update_auth(config)
    except Exception as e:
        st.error(e)