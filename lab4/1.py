def list_operations(a: list, b: list) -> list[set]:
    a = set(a)
    b = set(b)
    return [a & b, a | b, a - b, b - a]

a = [1, 1, 2, 2, 3]
b = [3, 3, 5, 5, 6, 6]

print(list_operations(a, b))
