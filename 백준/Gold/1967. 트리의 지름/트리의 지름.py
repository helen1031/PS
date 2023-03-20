import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
visited = [-1] * (n + 1)

def dfs(x, cost):
    for i in graph[x]:
        nx, ncost = i
        if visited[nx] == -1:
            visited[nx] = cost + ncost 
            dfs(nx, cost + ncost)

visited[1] = 0
dfs(1, 0)

maxstart, maxcost = 0, 0
for i in range(1, n + 1):
    if visited[i] > maxcost:
        maxcost = visited[i]
        maxstart = i
        
visited = [-1] * (n + 1)
visited[maxstart] = 0
dfs(maxstart, 0)

print(max(visited))
