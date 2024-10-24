import json

with open('classwork/lab3/studenti.json', 'r') as f:
    data = json.load(f)

cnt = 0
for student in data.values():
    nota = sum(student['seminarii']) / len(student['seminarii']) * 0.2
    examene = (student['curs'] + student['partial']) * 0.03
    proiect = student['proiect'] / 7 * 0.2

    media = nota + examene + proiect
    if media >= 4.5:
        cnt += 1

print(cnt)
    