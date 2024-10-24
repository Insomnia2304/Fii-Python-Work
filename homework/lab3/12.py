def group_by_rhyme(words: list[str]) -> list[list[str]]:
    ans = {}
    
    for word in words:
        if word[-2:] in ans:
            ans[word[-2:]] += [word]
        else:
            ans[word[-2:]] = [word]

    return list(ans.values())

print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))
