from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
boxes = [i for i in range(h)]
for i in range(h):
    box = []
    for _ in range(n):
        box.append(list(map(int, input().split())))
    boxes[i] = box

tmp = deque()
tomato = 0
day = 0
for z in range(h):
    box = boxes[z]
    for y in range(n):
        for x in range(m):
            if box[y][x] == 1:
                tmp.append((day, z, y, x))
            elif box[y][x] == 0:
                tomato += 1

while tmp:
    dd, nz, ny, nx = tmp.popleft()
    if dd != day:
        day = dd
    if ny - 1 >= 0 and boxes[nz][ny - 1][nx] == 0:
        boxes[nz][ny - 1][nx] = 1
        tomato -= 1
        tmp.append((dd + 1, nz, ny - 1, nx))
    if ny + 1 < n and boxes[nz][ny + 1][nx] == 0:
        boxes[nz][ny + 1][nx] = 1
        tomato -= 1
        tmp.append((dd + 1, nz, ny + 1, nx))
    if nx - 1 >= 0 and boxes[nz][ny][nx - 1] == 0:
        boxes[nz][ny][nx - 1] = 1
        tomato -= 1
        tmp.append((dd + 1, nz, ny, nx - 1))
    if nx + 1 < m and boxes[nz][ny][nx + 1] == 0:
        boxes[nz][ny][nx + 1] = 1
        tomato -= 1
        tmp.append((dd + 1, nz, ny, nx + 1))
    if nz + 1 < h and boxes[nz + 1][ny][nx] == 0:
        boxes[nz + 1][ny][nx] = 1
        tomato -= 1
        tmp.append((dd + 1, nz + 1, ny, nx))
    if nz - 1 >= 0 and boxes[nz - 1][ny][nx] == 0:
        boxes[nz - 1][ny][nx] = 1
        tomato -= 1
        tmp.append((dd + 1, nz - 1, ny, nx))

if tomato != 0:
    print(-1)
else:
    print(day)