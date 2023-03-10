
n, b = map(int, input().split())

def multiplyMatrix(matrix1, matrix2):
    res = [[0 for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            for k in range(n):
                res[y][x] += matrix1[y][k] * matrix2[k][x]
            res[y][x] %= 1000
    return res

def calculate(x, matrix):
    if x == 1:
        for y in range(n):
            for x in range(n):
                matrix[y][x] %= 1000
        return matrix
    
    tmp = calculate(x // 2, matrix)
    
    if x % 2 == 0:
        return multiplyMatrix(tmp, tmp)
    else:
        return multiplyMatrix(multiplyMatrix(tmp, tmp), matrix)
        
        
matrix = [list(map(int, input().split())) for _ in range(n)]
res = calculate(b, matrix)
for r in res:
    print(*r)