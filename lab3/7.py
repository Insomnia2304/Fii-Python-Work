def pal(numbers: list[int]) -> tuple[int,int]|int:
    cnt = 0
    grt = -1
    for number in numbers:
        if str(number) == str(number)[::-1]:
            cnt += 1
            grt = max(grt, number)
    return (cnt, grt) if cnt else cnt

print(pal([123, 121, 12321, 12345, 12321, 123, -0]))
print(pal([1234, 1214, 123454, 1234]))
