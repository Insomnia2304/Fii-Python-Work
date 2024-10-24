def x_times(*args: list, x: int) -> list:
    occurences = {}
    for arg in args:
        for element in arg:
            if element in occurences:
                occurences[element] += 1
            else:
                occurences[element] = 1
    return [element for element, occurence in occurences.items() if occurence == x]

print(x_times([1, 2, 3], [2, 3, 4], [4, 5, 6], [4,1, "test"], x=2))
