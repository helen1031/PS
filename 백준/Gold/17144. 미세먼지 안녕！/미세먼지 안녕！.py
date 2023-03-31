import sys
input = sys.stdin.readline

import copy

r, c, t = map(int, input().split())  # r행 c열
graph = [list(map(int, input().split())) for _ in range(r)]
up, down = 0, 0
for i in range(r):
    if graph[i][0] == -1:
        up = i
        down = i + 1
        break

def dust_spread(y, x):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    amount = graph[y][x] // 5
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < r and 0 <= nx < c and graph[ny][nx] != -1:
            tmp[ny][nx] += amount
            tmp[y][x] -= amount


air_y = [[0, -1, 0, 1], [0, 1, 0, -1]]
air_x = [[1, 0, -1, 0], [1, 0, -1, 0]]

def air_clean(ax, isdown):
    dy = air_y[isdown]
    dx = air_x[isdown]
    direction = 0

    y, x = ax, 1
    prv = 0
    next = graph[y][x]
    while True:
        if y == ax and x == 0:
            return
        ny, nx = y + dy[direction], x + dx[direction]
        if 0 <= ny < r and 0 <= nx < c:
            ntmp = graph[ny][nx]
            graph[ny][nx] = next
            graph[y][x] = prv
            next = ntmp
            y, x = ny, nx
            prv = graph[y][x]
        else:
            direction += 1

    graph[y][x] = ttmp

while t > 0:
    tmp = copy.deepcopy(graph)
    for y in range(r):
        for x in range(c):
            if graph[y][x] != -1 and graph[y][x] != 0:
                dust_spread(y, x)
    graph = copy.deepcopy(tmp)

    air_clean(up, 0)
    air_clean(down, 1)

    graph[up][0] = -1
    graph[down][0] = -1

    t -= 1

answer = 0
for y in range(r):
    for x in range(c):
        if graph[y][x] != -1:
            answer += graph[y][x]

print(answer)