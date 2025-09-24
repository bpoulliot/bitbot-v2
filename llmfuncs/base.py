import re
import pandas as pd
import ollama as ol
from config import Config

def create_client():
    client = ol.Client(host=Config.OLLAMA_HOST)
    return client

def get_models():
    client = create_client()
    excl_string="embed|embedding"
    avail_models = client.list()
    all_models = list(model["model"] for model in avail_models["models"])
    model_list = [m for m in all_models if not re.search(r'\b' + excl_string + r'\b', m)]
    return model_list

def stream_parse(stream):
    for chunk in stream:
        yield chunk['message']['content']

def send_chat(client, sys_prompt, prompt, model):
    stream = client.chat(
        model=model,
        messages=[{"role": "system", "content": sys_prompt},
                  {"role": "user", "content": prompt}],
        stream=True,
    )
    return stream

#def read_file(file):
#    dataframe = pd.read_csv(file)
#    st.write(dataframe)
#    return dataframe