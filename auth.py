import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import authfuncs.authenticate as auth

with st.spinner("Please wait..."):
    config = auth.config_auth()
    authenticator=auth.init_auth(config)
    auth.login(authenticator)
   
auth.update_auth(config)

with st.sidebar:
    st.markdown("# User")
    if st.session_state.get('authentication_status'):
        authenticator.logout()
        st.Page("pages/chat.py")
        st.Page("pages/settings.py")
        if st.button("Chat"):
            st.switch_page("chat.py")
        if st.button("Settings"):
            st.switch_page("settings.py")
    elif st.session_state.get('authentication_status') is False:
        st.error('Username/password is incorrect')
    elif st.session_state.get('authentication_status') is None:
        st.warning('Please enter your username and password')

if st.session_state.get('authentication_status'):
    st.title(f'Welcome *{st.session_state.get("name")}*')
elif st.session_state.get('authentication_status') is False:
    st.error('Username/password is incorrect')
elif st.session_state.get('authentication_status') is None:
    st.warning('Please enter your username and password')

# zj4F8dF5%$7XSz2@