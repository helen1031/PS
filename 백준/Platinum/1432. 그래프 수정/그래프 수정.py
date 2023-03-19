import sys
input = sys.stdin.readline

import heapq

n = int(input())
tmp = [list(map(int, input().rstrip())) for _ in range(n)]
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for y in range(1, n + 1):
    for x in range(1, n + 1):
        if tmp[y-1][x-1] == 1:
            #graph[y].append(x)
            #indegree[x] += 1
            graph[x].append(y)
            indegree[y] += 1

q = []
for i in range(1, n + 1):
    if indegree[i] == 0:
        #q.append(i)
        heapq.heappush(q, -i)

result = []

while q:
    #now = q.popleft()
    now = -heapq.heappop(q)
    result.append(now)

    for next in graph[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            #q.append(next)
            heapq.heappush(q, -next)

answer = [[] for _ in range(n + 1)]
if len(result) != n:
    print(-1)
else:
    for idx, node in enumerate(result):
        answer[node] = n - idx
    print(*answer[1:])
