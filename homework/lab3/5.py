def matrix_replace(matrix: list[list[int]]) -> list[list[int]]:
    no_lines = len(matrix)

    for i in range(no_lines):
        for j in range(i):
            matrix[i][j] = 0

    return matrix

print(matrix_replace(
[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]))
