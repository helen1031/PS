import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, t, d = map(int,input().split())
height = [list(input().strip()) for _ in range(n)]

for y in range(n):
    for x in range(m):
        if 'A' <= height[y][x] <= 'Z':
            height[y][x] = ord(height[y][x]) - ord('A')
        else:
            height[y][x] = ord(height[y][x]) - ord('a') + 26

graph = [[INF] * (n* m) for _ in range(n * m)]
for i in range(n * m):
    graph[i][i] = 0
    
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
    
for y in range(n):
    for x in range(m):
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if abs(height[ny][nx] - height[y][x]) > t:
                    graph[y * m + x][ny * m + nx] = INF
                elif height[ny][nx] <= height[y][x]:
                    graph[y * m + x][ny * m + nx] = 1
                else:
                    graph[y * m + x][ny * m + nx] = (height[ny][nx] - height[y][x]) ** 2
                    
for k in range(n*m):
    for a in range(n*m):
        for b in range(n*m):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    
maxheight = 0
for i in range(n*m):
    if graph[0][i] + graph[i][0] <= d:
        maxheight = max(maxheight, height[i // m][i % m])
    
print(maxheight)