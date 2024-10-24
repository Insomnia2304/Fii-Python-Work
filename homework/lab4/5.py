def validate_dict(s, d):
    for k, v in d.items():
        found_flag = False
        for rule in s:
            if rule[0] == k:
                found_flag = True
                break
        if not found_flag:
            return False
        if not(v.startswith(rule[1]) and v.endswith(rule[3]) and rule[2] in v):
            return False
    return True
print(validate_dict(s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}, d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"}))
