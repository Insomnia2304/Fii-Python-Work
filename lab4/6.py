def dup_count(list):
    return len(set(list)), len(list) - len(set(list))

print(dup_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(dup_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
