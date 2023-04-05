def text2text(text: str = "Заходят как-то в бар") -> str:
    import ruprompts
    from transformers import pipeline
    ppln = pipeline("text-generation-with-prompt", prompt="konodyuk/prompt_rugpt3large_joke")
    a = ppln(text)
    return a
