def count_set_bits(n: int) -> int:
    return bin(n).count('1')

n = 24

print(count_set_bits(n))
