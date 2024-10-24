def dict_to_freq(string: str):
    return {char: string.count(char) for char in string}

print(dict_to_freq('Ana has apples'))
