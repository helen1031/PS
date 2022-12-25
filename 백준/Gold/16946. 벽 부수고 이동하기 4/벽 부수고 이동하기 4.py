from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dic = {}
group = 1

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x):
    global group
    q = deque()
    q.append((y, x))
    visited[y][x] = group
    cnt = 1
    
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == "0" and not visited[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = group
                    cnt += 1
                    
    dic[group] = cnt
                    
for y in range(n):
    for x in range(m):
        if graph[y][x] == "0" and not visited[y][x]:
            bfs(y, x)
            group += 1
            
for y in range(n):
    for x in range(m):
        if graph[y][x] == "1":
            tmp = 1
            groups = []
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == "0":
                    if visited[ny][nx] not in groups:
                        tmp += dic[int(visited[ny][nx])]
                        groups.append(visited[ny][nx])
            graph[y][x] = str(tmp)
        
for y in range(n):
    for x in range(m):
        graph[y][x] = str(int(graph[y][x]) % 10)
    
    print("".join(graph[y]))