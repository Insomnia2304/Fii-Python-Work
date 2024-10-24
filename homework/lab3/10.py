def mix_lists(*args) -> list[tuple]:
    max_len = max(len(arg) for arg in args)
    ans = []

    for i in range(max_len):
        ans.append(tuple(arg[i] if i < len(arg) else None for arg in args))
    
    return ans

print(mix_lists([1, 2, 3], [5, 6, 7, 9], ["a", "b", "c"]))
