import streamlit as st
from llmfuncs import base as lf
import streamlit_authenticator as stauth

def authenticated_menu(authenticator):
    st.sidebar.page_link("pages/chat.py", label="Chat")
    st.sidebar.page_link("pages/settings.py", label="Settings")
    st.sidebar.page_link("pages/logout.py", label="Logout")
    return

def unauthenticated_menu():
    # Show a navigation menu for unauthenticated users
    st.sidebar.page_link("auth.py", label="Login")
    st.sidebar.page_link("pages/forgot_password.py", label="Forgot Password")

def menu(authenticator):
    if st.session_state.get('authentication_status') is False:
        st.error('Username/password is incorrect')
        unauthenticated_menu()
        return
    elif st.session_state.get('authentication_status') is None:
        unauthenticated_menu()
        return
    authenticated_menu(authenticator)

def menu_with_redirect(authenticator):
    # Redirect users to the main page if not logged in, otherwise continue to
    # render the navigation menu
    if st.session_state.get('authentication_status') is True:
        st.switch_page("pages/chat.py")
    menu(authenticator)