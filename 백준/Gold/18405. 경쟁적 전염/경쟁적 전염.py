import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())
tube = [list(map(int, input().split())) for _ in range(n)]

viruses = []
for y in range(n):
    for x in range(n):
        if tube[y][x] != 0:
            viruses.append((tube[y][x], y, x, 0))
viruses.sort()

s, i, j = map(int, input().split()) # i 행, j 열

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    q = deque(viruses)

    while q:
        vnum, vy, vx, time = q.popleft()

        if time == s:
            return

        for i in range(4):
            ny = vy + dy[i]
            nx = vx + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if tube[ny][nx] == 0:
                    tube[ny][nx] = vnum
                    q.append((vnum, ny, nx, time + 1))

bfs()
print(tube[i-1][j-1])