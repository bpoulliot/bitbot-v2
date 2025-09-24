import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

def config_auth():
    with open('authfuncs/config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
    return(config)

def init_auth(config):   
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
    )
    return authenticator

def login(authenticator):
    try:
        authenticator.login()
    except Exception as e:
        st.error(e)
    if st.session_state.get('authentication_status'):
        st.switch_page("pages/chat.py")

def verify_auth(authenticator):
    try:
        authenticator.login(location="unrendered")
    except Exception as e:
        st.error(e)

def auth_check():
    if not st.session_state.get('authentication_status'):
        st.switch_page("auth.py")

def update_auth(config):
    with open('authfuncs/config.yaml', 'w') as file:
        yaml.dump(config, file, default_flow_style=False, allow_unicode=True)

def authenticate():
    with st.spinner("Loading..."):
        config = config_auth()
        authenticator=init_auth(config)
        verify_auth(authenticator)
    update_auth(config)
    return authenticator