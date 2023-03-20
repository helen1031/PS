import sys
input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v + 1)]
for _ in range(v):
    tmp = list(map(int, input().split()))
    node = tmp[0]
    for i in range(1, len(tmp) - 2, 2):
        graph[node].append((tmp[i], tmp[i+1]))

visited = [-1] * (v + 1)
def dfs(x, cost):
    for i in graph[x]:
        nx, ncost = i
        if visited[nx] == -1:
            visited[nx] = cost + ncost
            dfs(nx, cost + ncost)

visited[1] = 0
dfs(1, 0)

maxnode, maxcost = 0, 0
for i in range(1, v + 1):
    if maxcost < visited[i]:
        maxnode = i
        maxcost = visited[i]
        
visited = [-1] * (v + 1)
visited[maxnode] = 0
dfs(maxnode, 0)

print(max(visited))