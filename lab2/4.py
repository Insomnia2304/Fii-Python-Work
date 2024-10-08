camel_string = 'UpperCamelCase'

ans = camel_string[0].lower()
for chr in camel_string[1:]:
    if chr.isupper():
        ans += '_'
    ans += chr.lower()

print(ans)
