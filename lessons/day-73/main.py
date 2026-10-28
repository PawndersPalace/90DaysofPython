def repeat_word(word: str, times: int) -> str:
    """Return a word repeated with spaces between copies."""
    return " ".join([word] * times)


message = repeat_word("practice", 3)
print(message)
