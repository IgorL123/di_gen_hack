import openai
import os

prompt = ""
os.environ['OPENAI_API_KEY'] = "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"

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


print(
text2text(
"C++, низкоуровневое программирование, ассемблер, Git, GitHub, MySQL, PostgerSQL, Go, React, команда, разработчик, Москва Сити, конкуренция"
)
)
