def compose(notes: list[str], moves: list[int], start: int) -> list[str]:
    ans = [notes[start]]
    for move in moves:
        start += move
        ans += [notes[start % len(notes)]]
    return ans

print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
