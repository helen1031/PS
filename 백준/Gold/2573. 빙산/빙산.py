import sys
input = sys.stdin.readline
#sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
check = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
            
def dfs(sy, sx):
    st = []
    st.append((sy, sx))
    
    while st:
        cur = st.pop()
        y, x = cur[0], cur[1]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 0:
                    check[y][x] += 1
                elif graph[ny][nx] != 0 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    #dfs(ny, nx)
                    st.append((ny, nx))

hmax = 0
for g in graph:
    hmax = max(hmax, max(g))

year = 0
while True:
    cnt = 0
    for y in range(1, n-1):
        for x in range(1, m-1):
            if graph[y][x] != 0:
                if not visited[y][x]:
                    cnt += 1
                    visited[y][x] = True
                    dfs(y, x)
                    
    if cnt > 1:
        print(year)
        break
    elif cnt == 0:
        print(0)
        break
    
    for y in range(1, n-1):
        for x in range(1, m-1):
            if visited[y][x]:
                visited[y][x] = False
            if graph[y][x] > 0:
                graph[y][x] = graph[y][x] - check[y][x]
                check[y][x] = 0
                if graph[y][x] < 0 :
                    graph[y][x] = 0
                    
    year += 1
    
    