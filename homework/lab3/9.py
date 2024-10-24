def cannot_see(heights: list[list[int]]) -> list[tuple[int,int]]:
    if not heights: return []
    ans = []
    lines = len(heights)
    columns = len(heights[0])

    for j in range(columns):
        max_height = -1
        for i in range(lines):
            if heights[i][j] <= max_height:
                ans += [(i, j)]
            max_height = max(max_height, heights[i][j])
    return ans

print(cannot_see([[1, 2, 3, 2, 1, 1],
 [2, 4, 4, 3, 7, 2],
 [5, 5, 2, 5, 6, 4],
 [6, 6, 7, 6, 7, 5]]))
