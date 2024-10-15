def list_operations(a: list, b: list) -> tuple[list, list, list, list]:
    return [x for x in a if x in b], a + [x for x in b if x not in a], [x for x in a if x not in b], [x for x in b if x not in a]

a = [1, 2, 3, 4, 5]
b = [4, 5, 6]

print(list_operations(a, b))
