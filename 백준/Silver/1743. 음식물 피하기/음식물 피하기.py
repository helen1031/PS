import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

n, m, k = map(int, input().split())
foods = [list(map(int, input().split())) for _ in range(k)] # 행 열

graph = [["."] * m for _ in range(n)]
for food in foods:
    y, x = food
    graph[y-1][x-1] = "#"

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

visited = [[False] * m for _ in range(n)]

tmp = 0
def dfs(y, x):
    global tmp

    tmp += 1
    visited[y][x] = True

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
            if graph[ny][nx] == "#":
                dfs(ny, nx)

maxsize = 0
for y in range(n):
    for x in range(m):
        if not visited[y][x] and graph[y][x] == "#":
            tmp = 0
            dfs(y, x)
            maxsize = max(maxsize, tmp)
print(maxsize)