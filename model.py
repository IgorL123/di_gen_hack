import openai
import os

prompt = ""

def get_promt():
    global prompt
    with open("promt.txt", "r", encoding="utf-8") as f:
        prompt = f.read()

def text2text(text: str) -> str:

    get_promt()

    openai.api_key = os.environ.get('OPENAI_API_KEY')
    pmt = prompt.format(**{'keywords':text})

    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=pmt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )
    text = completions.choices[0].text
    return text

