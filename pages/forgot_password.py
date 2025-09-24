import streamlit as st
import streamlit_authenticator as stauth
from authfuncs import authenticate as af
from menu import menu
from config import Config

st.set_page_config(
    page_icon=Config.PAGE_ICON,
    page_title=Config.FORGOT_TITLE,
    initial_sidebar_state=Config.SIDEBAR
)

st.title=Config.FORGOT_TITLE

authenticator = af.authenticate()

menu(authenticator)

st.info("Please enter your username to reset your password.")

try:
    username_of_forgotten_password, \
    email_of_forgotten_password, \
    new_random_password = authenticator.forgot_password(two_factor_auth=True, send_email=True)
    if username_of_forgotten_password:
        st.success('New password to be sent securely')
        config = af.config_auth()
        af.update_auth(config)
        # To securely transfer the new password to the user please see step 8.
    elif username_of_forgotten_password == False:
        st.error('Username not found')
except Exception as e:
    st.error(e)