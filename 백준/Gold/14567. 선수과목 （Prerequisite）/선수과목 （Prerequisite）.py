import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    
q = deque([])
semesters = [0] * (n + 1)
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append((i, 1))
        
while q:
    now, semester = q.popleft()
    semesters[now] = semester
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append((i, semester + 1))

print(*semesters[1:])