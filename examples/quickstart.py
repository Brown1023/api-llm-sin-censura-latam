# API de LLM sin censura para LATAM — compatible con OpenAI — quickstart
# pip install openai
import os
from openai import OpenAI

client = OpenAI(base_url="https://uncensored-llm.sbs/v1", api_key=os.environ["UNLLM_KEY"])
r = client.chat.completions.create(
    model="uncensored-llm",
    messages=[{"role": "user", "content": "Explica sin rodeos como se calcula el valor de mercado de una criptomoneda."}],
)
print(r.choices[0].message.content)
