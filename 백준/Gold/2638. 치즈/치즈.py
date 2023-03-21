import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def cheese_bfs(sy, sx):
    q = deque([(sy, sx)])
    cheese_visited[sy][sx] = 0

    while q:
        y, x = q.popleft()
        aircnt = 0
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 2:
                    aircnt += 1
                elif cheese_visited[ny][nx] == -1 and graph[ny][nx] == 1:
                    q.append((ny, nx))
                    cheese_visited[ny][nx] = cheese_visited[y][x] + 1

        if aircnt >= 2:
            graph[y][x] = 'C'

def air_dfs(y, x):
    air_visited[y][x] = True
    graph[y][x] = 2

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if not air_visited[ny][nx] and graph[ny][nx] == 0:
                air_dfs(ny, nx)


time = 0
while True:
    # 1. 내외부 공기를 판별한다 - 먼저 외부 공기 돌리면서 2로 바꿔주기(0 공기는 내부공기)
    air_visited = [[False] * m for _ in range(n)]
    cheese_visited = [[-1] * m for _ in range(n)]

    onlyair = True

    air_dfs(0, 0)
    for y in range(n):
        for x in range(m):
            if cheese_visited[y][x] == -1 and graph[y][x] == 1:
                onlyair = False
                cheese_bfs(y, x)

    if onlyair:
        break

    for y in range(n):
        for x in range(m):
            if graph[y][x] == 'C':
                graph[y][x] = 0
            elif graph[y][x] == 2:
                graph[y][x] = 0
    time += 1

print(time)