import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False] * (n + 1)

def bfs(start):
    q = deque([start])
    visited[start] = True
    
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    
bfs(1)
print(visited.count(True)-1)