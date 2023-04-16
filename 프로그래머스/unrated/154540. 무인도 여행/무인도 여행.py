from collections import deque

def solution(maps):
    answer = []
    
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    
    def bfs(sy, sx):
        q = deque()
        q.append((sy, sx))
        visited[sy][sx] = True
        cost = 0
        
        while q:
            y, x = q.popleft()
            cost += int(maps[y][x])
            
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
                    if maps[ny][nx] != "X" and not visited[ny][nx]:
                        q.append((ny, nx))
                        visited[ny][nx] = True
                        
        answer.append(cost)
                
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] != "X" and not visited[y][x]:
                bfs(y, x)
    
    if not answer:
        answer.append(-1)
    else:
        answer.sort()
    return answer