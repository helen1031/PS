import sys
input = sys.stdin.readline

from itertools import combinations
from collections import deque

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
vpossible = []
for y in range(n):
    for x in range(n):
        if lab[y][x] == 2:
            vpossible.append((y, x))
vcases = list(combinations(vpossible, m))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 바이러스 확산
def bfs(viruses):
    maxtime = 0
    visited = [[-1] * n for _ in range(n)]
    q = deque()

    for virus in viruses:
        visited[virus[0]][virus[1]] = 0
        q.append(virus)

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if lab[ny][nx] != 1 and visited[ny][nx] == -1:
                    q.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1
                    maxtime = max(maxtime, visited[ny][nx])

    for y in range(n):
        for x in range(n):
            if visited[y][x] == -1 and lab[y][x] == 0:
                return 51 * 51

    return maxtime

answer = 51 * 51
for case in vcases:
    answer = min(answer, bfs(case))

if answer == 51 * 51:
    print(-1)
else:
    print(answer)        
        