import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    tmp = list(map(int, input().split()))
    for i in range(1, len(tmp)-1):
        graph[tmp[i]].append(tmp[i+1])
        indegree[tmp[i+1]] += 1
        
q = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

result = []
cycle = False
for i in range(n):
    if not q:
        cycle = True
        break
    
    now = q.popleft()
    result.append(now)
    
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

if cycle:
    print(0)
else:
    print(*result)