def ascii_div(strings: list[str], x: int = 1, flag=True) -> list[list[str]]:
    ans = []
    for string in strings:
        letters = []
        for letter in string:
            if flag:
                letters += [letter] if ord(letter) % x == 0 else []
            else:
                letters += [letter] if ord(letter) % x else []
        ans += [letters]
    return ans

print(ascii_div(["test", "hello", "lab002"], x = 2, flag = False))
