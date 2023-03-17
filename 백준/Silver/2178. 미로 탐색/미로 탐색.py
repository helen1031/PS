import sys
input = sys.stdin.readline

from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n, m = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

mincnt = m * n

def bfs(sy, sx, cnt): # n-1, m-1 도착지점
    global mincnt
    
    q = deque([(sy, sx, cnt)])
    visited[sy][sx] = True
    
    while q:
        cy, cx, ccnt = q.popleft()
        
        if cy == n - 1 and cx == m - 1:
            mincnt = min(mincnt, ccnt)

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < n and 0 <= nx < m and maze[ny][nx] == 1 and not visited[ny][nx]:
                q.append((ny, nx, ccnt + 1))
                visited[ny][nx] = True
        
bfs(0, 0, 1)
print(mincnt)