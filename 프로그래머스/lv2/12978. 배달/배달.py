import heapq

INF = int(1e9)

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)
    for r in road:
        a, b, c = r
        graph[a].append((b, c))
        graph[b].append((a, c))
    distance[1] = 0
    
    def dijk(start):
        q = []
        heapq.heappush(q, (0, start))
        
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
                
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
    dijk(1)
    cnt = 0
    for d in distance[1:]:
        if d <= K:
            cnt += 1 
    
    return cnt