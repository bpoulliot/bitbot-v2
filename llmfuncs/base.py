import re
import pandas as pd

def get_models(client):
    excl_string="embed"
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

def read_file(file):
    dataframe = pd.read_csv(file)
    st.write(dataframe)
    return dataframe