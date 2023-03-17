import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

hq = []    
start, goal = map(int, input().split())
heapq.heappush(hq, (0, start))
distance[start] = 0

while hq:
    cost, cur = heapq.heappop(hq)
    if cost > distance[cur] :
        continue
    for x in graph[cur]:
        pos, c = x[0], x[1]
        if cost + c < distance[pos]:
            distance[pos] = cost + c
            heapq.heappush(hq, (distance[pos], pos))
            
print(distance[goal])