def custom_sort(list_: list[tuple[str,str]]) -> list[tuple[str,str]]:
    return sorted(list_, key=lambda x: x[1][2])

print(custom_sort([('abc', 'bcd'), ('abc', 'zza')]))
