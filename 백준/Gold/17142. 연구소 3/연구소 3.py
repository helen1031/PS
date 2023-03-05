import sys
from collections import deque

input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

wallcnt = 0

def activeCases():
    global wallcnt
    virus = []

    for y in range(n):
        for x in range(n):
            if lab[y][x] == 2:
                virus.append((y, x))
            elif lab[y][x] == 1:
                wallcnt += 1

    nCr = list(combinations(virus, m))
    return nCr

def bfs(active):
    q = deque()
    visited = [[-1] * n for _ in range(n)]
    tmpres = 0

    for a in active:
        q.append(a)
        visited[a[0]][a[1]] = 0

    while q:
        vy, vx = q.popleft()

        for i in range(4):
            ny = vy + dy[i]
            nx = vx + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if lab[ny][nx] == 0 and visited[ny][nx] == -1:
                    visited[ny][nx] = visited[vy][vx] + 1
                    q.append((ny, nx))
                    tmpres = max(tmpres, visited[ny][nx])
                elif lab[ny][nx] == 2 and visited[ny][nx] == -1:
                    visited[ny][nx] = visited[vy][vx] + 1
                    q.append((ny, nx))

    walltmp = 0
    for v in visited:
        walltmp += v.count(-1)
    if walltmp != wallcnt:
        return 51 * 51
    else:
        return tmpres

result = 51 * 51
if m >= 1:
    cases = activeCases()
    for case in cases:
        result = min(result, bfs(list(case)))

    if result == 51 * 51:
        print(-1)
    else:
        print(result)
else:
    print(-1)