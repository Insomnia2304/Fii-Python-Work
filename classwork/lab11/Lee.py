from collections import deque
import zlib
from Crypto.Cipher import ARC4
import time

def rc4_decrypt(ciphertext, key):
    cipher = ARC4.new(key.encode())
    return cipher.decrypt(ciphertext).decode('utf-8', errors='ignore').replace('\r', '')

def find_key(mat: str):
    lines = mat.strip().split('\n')[1:]
    mat = [list(line) for line in lines]

    n = len(mat)
    m = len(mat[0])

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 'S':
                S = (i, j)
            if mat[i][j] == 'X':
                X = (i, j)

    # print(S, X)

    queue = deque([(S, '')])
    vis = [[False] * m for _ in range(n)]
    move = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    while queue:
        curr, path = queue.popleft()

        if curr == X:
            key = zlib.crc32(path.encode()) ^ 0xffffffff
            return f'{key:08X}'

        for dir, (dx, dy) in move.items():
            x, y = curr[0] + dx, curr[1] + dy
            if not vis[x][y] and mat[x][y] != '#':
                vis[x][y] = True
                queue.append(((x, y), path + dir))

prev = time.time()
for dir in ['1_21', '2_101', '3_301', '4_501', '5_1001', '6_1501', '7_2001', '8_2401']:
    for i in range(8):
        if (dir, i) == ('1_21', 0):
            with open(f'./classwork/lab11/{dir}/in_{i}.bin', 'r') as f:
                key = find_key(f.read())
        else:
            with open(f'./classwork/lab11/{dir}/in_{i}.bin', 'rb') as f:
                decrypted_data = rc4_decrypt(f.read(), key)
                key = find_key(decrypted_data)
            print(f'Finished {dir}/in_{i}.bin - Time spent: {time.time() - prev:.2f}s')
            prev = time.time()
                
print(f'Archive key: {key}')
