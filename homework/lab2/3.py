str1 = 'ana are banana'
str2 = 'ana'

cnt = 0
pos = str1.find(str2)
while pos != -1:
    cnt += 1
    pos = str1.find(str2, pos+1)

print(cnt)
