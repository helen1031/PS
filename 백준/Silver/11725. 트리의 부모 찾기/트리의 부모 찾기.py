import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n + 1)
parents = [1] * (n + 1)
    
def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            parents[i] = start
            dfs(i)
    
dfs(1)

for parent in parents[2:]:
    print(parent)