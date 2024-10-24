string = 'carrOt'

cnt = 0
for chr in string:
    if chr.lower() in 'aeiou':
        cnt += 1

print(cnt)
