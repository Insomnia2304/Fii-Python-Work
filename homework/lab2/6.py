def extract_first_number(text: str) -> int|None:
    for i in range(len(text)):
        if text[i].isdigit():
            for j in range(i, len(text)):
                if not text[j].isdigit():
                    return int(text[i:j])
            return int(text[i:])
    return None

text1 = 'An apple is 123 USD'
text2 = 'abc123abc'

print(extract_first_number(text1))
print(extract_first_number(text2))
