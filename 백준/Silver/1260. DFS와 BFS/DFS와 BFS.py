import sys
input = sys.stdin.readline

from collections import deque

n, m, v = map(int, input().split())

dvisited = [False] * (n+1)
bvisited = [False] * (n+1)

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
    graph[a].sort()
    graph[b].sort()

danswer = []
banswer = []

def dfs(start):
    dvisited[start] = True
    danswer.append(start)
    for i in graph[start]:
        if not dvisited[i]:
            dfs(i)

def bfs(start):
    q = deque([start])
    bvisited[start] = True
    
    while q:
        v = q.popleft()
        banswer.append(v)
        for i in graph[v]:
            if not bvisited[i]:
                q.append(i)
                bvisited[i] = True

dfs(v)
bfs(v)
print(*danswer)
print(*banswer)