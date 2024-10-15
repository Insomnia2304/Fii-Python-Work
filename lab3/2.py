def is_prime(x: int) -> bool:
    if x < 2:
        return False

    div = 2
    while div * div <= x:
        if x % div == 0:
            return False
        div += 1

    return True

def find_primes(input: list[int]) -> list[int]:
    return [x for x in input if is_prime(x)]

test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(find_primes(test))

test = [10, 20]
print(find_primes(test))
