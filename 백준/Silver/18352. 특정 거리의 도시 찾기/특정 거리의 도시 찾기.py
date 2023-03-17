import sys
input = sys.stdin.readline

from collections import deque

# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    
visited = [False] * (n + 1)
cities = []
    
# bfs
q = deque([(x, 0)])
visited[x] = True

while q:
    current, cost = q.popleft()
    
    if cost == k:
        cities.append(current)
        continue
        
    for i in graph[current]:
        if not visited[i]:
            q.append((i, cost + 1))
            visited[i] = True

if not cities:
    print(-1)
else:
    cities.sort()
    for city in cities:
        print(city)
