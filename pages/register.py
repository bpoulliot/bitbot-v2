import streamlit as st
import streamlit_authenticator as stauth
from authfuncs import authenticate as af
from menu import menu
from config import Config

st.set_page_config(
    page_icon=Config.PAGE_ICON,
    page_title=Config.REGISTER_TITLE,
    initial_sidebar_state=Config.SIDEBAR
)

st.title=Config.REGISTER_TITLE

authenticator = af.authenticate()

menu(authenticator)

config = af.config_auth()

try:
    email_of_registered_user, \
    username_of_registered_user, \
    name_of_registered_user = authenticator.register_user(pre_authorized=config['pre-authorized']['emails'])
    if email_of_registered_user:
        st.success('User registered successfully')
        af.update_auth(config)
except Exception as e:
    st.error(e)