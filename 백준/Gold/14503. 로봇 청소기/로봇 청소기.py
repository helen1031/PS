from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

lr = [0, -1, 0, 1]
lc = [-1, 0, 1, 0]

br = [1, 0, -1, 0]
bc = [0, -1, 0, 1]

cnt = 0
q = deque([])
q.append((r, c, d))

while q:
    r, c, d= q.popleft()
    if area[r][c] == 0:
        area[r][c] = -1
        cnt += 1

    qadd = 0
    for i in range(4):
        nr, nc = r + lr[d], c + lc[d]
        if 0 <= nr < n and 0 <= nc < m:
            if area[nr][nc] == 0:
                d -= 1
                if d < 0:
                    d += 4
                q.append((nr, nc, d))
                qadd = 1
                break
            else:
                d -= 1
                if d < 0:
                    d += 4
                continue

    if i == 3 and qadd == 0:
        nr, nc = r + br[d], c + bc[d]
        if area[nr][nc] != 1:
            q.append([nr, nc, d])

print(cnt)