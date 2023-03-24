import sys
input = sys.stdin.readline

n, m = map(int, input().split())
table = [[0] * (n + 1)]
for _ in range(n):
    tmp = [0] + list(map(int, input().split()))
    table.append(tmp)
    
for y in range(1, n +1):
    for x in range(1, n+1):
        table[y][x] = table[y][x-1] + table[y][x]
        
for x in range(1, n+1):
    for y in range(1, n+1):
        table[y][x] = table[y-1][x] + table[y][x]
        
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    a = table[x1-1][y1-1]
    b = table[x1-1][y2]
    c = table[x2][y1-1]
    d = table[x2][y2]
    print(d - b - c + a)