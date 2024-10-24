def dict_cmp(d1: dict, d2: dict):
    for (key1,key2) in zip(d1.keys(),d2.keys()):
        if type_cmp(key1,key2) is False:
            return False
    for (value1,value2) in zip(d1.values(),d2.values()):
        if type_cmp(value1,value2) is False:
            return False
    return True

def type_cmp(type1, type2):
    if type(type1) != type(type2):
        return False
    # Sequence, Set types
    if isinstance(type1, list) or isinstance(type1, tuple) or isinstance(type1, range) or isinstance(type1, set) or isinstance(type1, frozenset):
        for (item1, item2) in zip(type1, type2):
            if type_cmp(item1, item2) is False:
                return False
        return True
    # Dictionary
    if isinstance(type1, dict):
        return dict_cmp(type1, type2)
    # Simple types
    return type1 == type2

complex_dict1 = {
    42: "integer as key",  # Integer key, string value
    "string_key": [1, 2, 3, 4],  # String key, list value
    3.14: {"nested_float_key": "float as key"},  # Float key, dict value
    True: {False: "bool as key", None: "none as key"},  # Boolean keys and nested dict
    (1, 2): ["tuple as key", {"nested": ["more nesting", 123, (5, 6)]}],  # Tuple key with nested list and dict
    frozenset([1, 2, 3]): {1: "frozen set as key", "further_nested": {"deep": {}}},
    "nested_dict": {
        "level_1": {
            "level_2": {
                "level_3": ["deep list", {1: "deep dict", "x": 99.9}],
                "another_list": [(1, 2), 42, {"complexity": "increases"}],
            },
        },
    },
    "mixed_types": {
        10: [True, None, {"mix": [1, 2, "string", (1, 2)]}],
        False: {3.5: "float key", "inside_nested": [None, {"dict": {}}]},
    },
}

complex_dict2 = {
    42: "integer as key",  # Integer key, string value
    "string_key": [1, 2, 3, 4],  # String key, list value
    3.14: {"nested_float_key": "float as key"},  # Float key, dict value
    True: {False: "bool as key", None: "none as key"},  # Boolean keys and nested dict
    (1, 2): ["tuple as key", {"nested": ["more nesting", 123, (5, 6)]}],  # Tuple key with nested list and dict
    frozenset([1, 2, 3]): {1: "frozen set as key", "further_nested": {"deep": {}}},
    "nested_dict": {
        "level_1": {
            "level_2": {
                "level_3": ["deep list", {1: "deep dict", "x": 99.9}],
                "another_list": [(1, 2), 42, {"complexity": "increases"}],
            },
        },
    },
    "mixed_types": {
        10: [True, None, {"mix": [1, 2, "string", (1, 2)]}],
        False: {3.5: "float key", "inside_nested": [None, {"dict": {}}]},
    },
}

print(dict_cmp(complex_dict1, complex_dict2))
