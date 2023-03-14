n = int(input())

def multiplyMatrix(mat1, mat2):
    l = len(mat1)
    res = [[0 for _ in range(l)] for _ in range(l)]
    for y in range(l):
        for x in range(l):
            for k in range(l):
                res[y][x] += mat1[y][k] * mat2[k][x]
            res[y][x] %= 1000000007
    return res

def calculate(x, matrix):
    if x == 1:
        for y in range(len(matrix)):
            for x in range(len(matrix)):
                matrix[y][x] %= 1000000007
        return matrix
    
    tmp = calculate(x//2, matrix)
    
    if x % 2 == 0:
        return multiplyMatrix(tmp, tmp)
    else:
        return multiplyMatrix(multiplyMatrix(tmp, tmp), matrix)
    

matrix = [[1, 1], [1, 0]]
res = calculate(n, matrix)
print(res[0][1])