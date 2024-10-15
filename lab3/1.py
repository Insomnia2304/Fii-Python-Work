def first_n_fib(n: int) -> list[int]:
    ans = [0, 1]

    if n < 2:
        return ans[:n]
    
    for i in range(2, n):
        ans += [ans[i-1] + ans[i-2]]

    return ans
