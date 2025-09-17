import streamlit as st
import ollama
from time import sleep

st.subheader("Model Management", divider="red", anchor=False)

st.subheader("Download Models", anchor=False)
model_name = st.text_input(
    "Enter model name from https://ollama.com/library to download:", placeholder="mistral:7b"
)
if st.button(f"📥 :green[**Download**] :red[{model_name}]"):
    if model_name:
        try:
            ollama.pull(model_name)
            st.success(f"Downloaded model: {model_name}", icon="🎉")
            st.balloons()
            sleep(1)
            st.rerun()
        except Exception as e:
            st.error(
                f"""Failed to download model: {
                model_name}. Error: {str(e)}""",
                icon="😳",
            )
    else:
        st.warning("Please enter a model name.", icon="⚠️")