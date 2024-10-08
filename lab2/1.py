def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)

x = input('Enter a list of numbers separated by space: ').split()

if len(x) < 2:
    exit('List must contain at least 2 numbers')

ans = gcd(int(x[0]), int(x[1]))

for i in range(2, len(x)):
    ans = gcd(ans, int(x[i]))

print(ans)