import sys
input = sys.stdin.readline

def find_parent(parent, cur):
    if parent[cur[0]][cur[1]][0] != cur[0] and parent[cur[0]][cur[1]][1] != cur[1]:
        parent[cur[0]][cur[1]] = find_parent(parent, parent[cur[0]][cur[1]])
    return parent[cur[0]][cur[1]]
    
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    tmp = [a, b]
    tmp.sort()
    
    parent[tmp[1][0]][tmp[1][1]] = tmp[0]

direction = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

n, m = map(int, input().split())
graph = [list(map(str, input().rstrip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
parent = [[(y, x) for x in range(m)] for y in range(n)]
safezone = 0

def dfs(sy, sx):
    global safezone
    
    visited[sy][sx] = True
    
    ny = sy + direction[graph[sy][sx]][0]
    nx = sx + direction[graph[sy][sx]][1]
    
    if 0 <= ny < n and 0 <= nx < m:
        if not visited[ny][nx]:
            union_parent(parent, (sy, sx), (ny, nx))
            dfs(ny, nx)
        else:
            # 동일 집합 cycle
            if find_parent(parent, (ny, nx)) == find_parent(parent, (sy, sx)):
                safezone += 1
            # 타 cycle 편입가능
            else:
                safezone += 0
            
for y in range(n):
    for x in range(m):
        if not visited[y][x]:
            dfs(y, x)
            
print(safezone)