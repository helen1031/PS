from collections import deque

global g, s

def bfs(v):
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque(v)

    while q:
        vno, vx, vy, vs = q.popleft()

        if s == vs:
            break

        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                if g[nx][ny] == 0:
                    g[nx][ny] = vno
                    q.append((vno, nx, ny, vs+1))

n, k = map(int, input().split())
g= []
v = []
for i in range(n):
    g.append(list(map(int, input().split())))
    for j in range(n):
        if g[i][j] != 0 : # 바이러스 존재
            v.append((g[i][j], i, j, 0))

v.sort()    #바이러스 번호 오름차순
s, x, y = map(int, input().split())

bfs(v)
print(g[x-1][y-1])
