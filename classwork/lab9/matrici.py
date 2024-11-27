import time
start = time.time()

n = file = 2000

with open(f'./matrici/result_{file}.txt') as f:
    data = f.read()

data = data.split()
data = [set(x.strip("{}").split(',')) for x in data]

M_res = [data[i:i+n] for i in range(0, n*n, n)]

print(f'End res parsing: {time.time()-start}')
with open(f'./matrici/matrici_{file}.txt') as f:
    data = f.read()

m1, m2 = data.split('\n\n')
print(f'End split: {time.time()-start}')


m1 = [set(x.strip("{}").split(',')) for x in m1.split()]
print(f'End m1: {time.time()-start}')


m2 = [set(x.strip("{}").split(',')) for x in m2.split()]
print(f'End m2: {time.time()-start}')

M1 = [m1[i:i+n] for i in range(0, n*n, n)]
M2 = [m2[i:i+n] for i in range(0, n*n, n)]
print(f'End parsing: {time.time()-start}')


M3 = [[M1[lin][col].intersection(M2[lin][col]) for col in range(n)] for lin in range(n)]
print(f'End intersection: {time.time()-start}')

for lin in range(n):
    for col in range(n):
        # sorted(M3[lin][col])
        if len(M3[lin][col]) == 0:
            M3[lin][col] = {''}

with open('result.txt', 'w') as f:
    f.write(str(M3)) 

print(M_res == M3)
end = time.time()
print(f'Total time for size {n}: {end - start}')
# print(f'Time for data read: {citire - start}')
# print(f'Time for intersection: {end_intersection - citire}')
