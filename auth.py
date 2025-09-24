import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import authfuncs.authenticate as af
from menu import menu
from config import Config

st.set_page_config(
    page_icon=Config.PAGE_ICON,
    page_title=Config.AUTH_TITLE,
    initial_sidebar_state=Config.SIDEBAR
)

st.title=Config.AUTH_TITLE

authenticator = af.authenticate()

menu(authenticator)

st.info("Enter your username and password to login.")

af.login(authenticator)

register, forgot = st.columns(2)

with register:
    st.page_link("pages/register.py", label="Register for an Account")

with forgot:
    st.page_link("pages/forgot_password.py", label="Forgot Password")

