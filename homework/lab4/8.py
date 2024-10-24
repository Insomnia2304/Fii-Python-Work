def loop(mapping: dict) -> list[str]:
    items = [mapping['start']]
    
    while items[-1] in mapping and mapping[items[-1]] != items[-1]:
        items += [mapping[items[-1]]]

    return items

print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
