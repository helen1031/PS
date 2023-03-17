import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
rooms = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[-1] * n for _ in range(n)]

sy, sx = 0, 0
ey, ex = n - 1, n - 1

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

q = deque([(sy, sx, 1)])
visited[sy][sx] = 0

while q:
    y, x, color = q.popleft()
    
    if y == ey and x == ex:
        break
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == -1:
            if rooms[ny][nx] == 1:
                q.appendleft((ny, nx, 1))
                visited[ny][nx] = visited[y][x]
            else:
                q.append((ny, nx, 0))
                visited[ny][nx] = visited[y][x] + 1
                
print(visited[ey][ex])
                