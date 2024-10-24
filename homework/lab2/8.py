def count_words(text: str) -> int:
    return len(text.split())

text = 'I have Python exam'

print(count_words(text))
