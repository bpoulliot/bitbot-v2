import streamlit as st
import streamlit_authenticator as stauth
from authfuncs import authenticate as af
from menu import menu
from config import Config

st.set_page_config(
    page_icon=Config.PAGE_ICON,
    page_title=Config.LOGOUT_TITLE,
    initial_sidebar_state=Config.SIDEBAR
)

st.title=Config.LOGOUT_TITLE

af.auth_check()

authenticator = af.authenticate()

menu(authenticator)

st.title("Logout of Bitbot Chat?", anchor=False)

with st.container(horizontal_alignment="center"):
    authenticator.logout(location="main")
#    if st.session_state.get('authentication_status') is None:
#        st.switch_page("auth.py")