class Matrix:
    def __init__(self, N, M):
        self.__m = []
        self.__N = N
        self.__M = M

        self.__m += [[0] * M for _ in range(N)]

    def set_element(self, i, j, value):
        self.__m[i][j] = value
    
    def get_element(self, i, j):
        return self.__m[i][j]
    
    def get_N(self):
        return self.__N
    
    def get_M(self):
        return self.__M
    
    def __str__(self):
        _str = ''
        for i in range(self.__N):
            for j in range(self.__M):
                _str += str(self.__m[i][j]) + ' '
            _str += '\n'
        return _str[:-1] # remove last newline
    
    def get_transpose(self):
        t = Matrix(self.__M, self.__N)
        for i in range(self.__N):
            for j in range(self.__M):
                t.set_element(j, i, self.__m[i][j])
        return t
        
    @staticmethod
    def mul(m1, m2):
        if m1.get_M() != m2.get_N():
            return None
        res = Matrix(m1.get_N(), m2.get_M())
        for i in range(m1.get_N()):
            for j in range(m2.get_M()):
                for k in range(m1.get_M()):
                    res.set_element(i, j, res.get_element(i, j) + m1.get_element(i, k) * m2.get_element(k, j))
        return res
    
    def transform(self, func):
        for i in range(self.__N):
            for j in range(self.__M):
                self.__m[i][j] = func(self.__m[i][j])

m = Matrix(3,3)
for i in range(3):
    for j in range(3):
        m.set_element(i, j, i * 3 + j)
print(m)

n = Matrix(3,3)
for i in range(3):
    for j in range(3):
        n.set_element(i, j, i * 3 + j)
print(n)

print(Matrix.mul(m, n))

m.transform(lambda x: x * 2)
print(m)
