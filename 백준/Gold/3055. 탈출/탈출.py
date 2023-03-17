import sys
input = sys.stdin.readline

from collections import deque

r, c = map(int, input().split()) # r행 c열
world = [list(input().rstrip()) for _ in range(r)]
visited = [[-1] * c for _ in range(r)]

q = deque([])
sy, sx, ey, ex = 0, 0, 0, 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 물 먼저 이동하고 고슴도치 이동
for y in range(r):
    for x in range(c):
        if world[y][x] == 'S':
            sy, sx = y, x
            q.append((sy, sx))
            visited[sy][sx] = 0
        elif world[y][x] == 'D':
            ey, ex = y, x
        elif world[y][x] == '*':
            q.appendleft((y, x))
            visited[y][x] = 0
        
while q:
    y, x = q.popleft()
    
    if world[ey][ex] == "S":
        print(visited[ey][ex])
        exit()
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < r and 0 <= nx < c and visited[ny][nx] == -1:
            if world[y][x] == 'S':
                if world[ny][nx] == '.' or world[ny][nx] == "D":
                    q.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1
                    world[ny][nx] = world[y][x]
                    
            elif world[y][x] == '*':
                if world[ny][nx] == '.' or world[ny][nx] == 'S':
                    q.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1
                    world[ny][nx] = world[y][x]
                    
print("KAKTUS")