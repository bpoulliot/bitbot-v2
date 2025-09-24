# Authored by: Brandon Poulliot

class Config:
    PAGE_TITLE = "BitBot Chat"
    OLLAMA_HOST = "http://192.168.1.229:11434"
    DEFAULT_MODEL = "llama3.1:8b"
    SIDEBAR = "collapsed"
    PAGE_ICON = ":material/chat:"
    CHAT_TITLE = "Bitbot | Chat"
    REGISTER_TITLE = "Bitbot | Register"
    LOGOUT_TITLE = "Bitbot | Logout"
    FORGOT_TITLE = "Bitbot | Forgot Password"
    AUTH_TITLE = "Bitbot | Login"
    SETTINGS_TITLE = "Bitbot | Settings"
    SYSTEM_PROMPT = """You are a helpful chatbot that answers user questions.
                    You should respond in a concise manner with a jocular tone.
                    Provide citations if necessary, but ensure they are correct."""