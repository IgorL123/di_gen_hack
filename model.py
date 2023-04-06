import openai
import os
prompt = "Генерация текста на русском языке на основе ключевых слов. Генерировать должность, обязанности и требования: "


def text2text(text: str) -> str:
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    pmt = prompt + f"{text}"
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

