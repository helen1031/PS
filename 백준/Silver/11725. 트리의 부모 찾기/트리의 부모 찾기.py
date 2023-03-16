import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
visited = [False] * (n+1)
parent = [1 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append((1, 1))
visited[1] = True

while q:
    cur, par = q.popleft()
    parent[cur] = par
    if graph[cur]:
        for i in graph[cur]:
            if not visited[i]:
                q.append((i, cur))
                visited[i] = True
            
for i in range(2, n+1):
    print(parent[i])