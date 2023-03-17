import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
visited = [-1] * 100 * 10000
q = deque([])
for coin in coins:
    q.append(coin)
    visited[coin] = 1

while q:
    cost = q.popleft()
    
    if cost == k:
        print(visited[cost])
        exit()
    
    if cost > k:
        continue
        
    for coin in coins:
        ncost = cost + coin
        if visited[ncost] == -1:
            q.append(ncost)
            visited[ncost] = visited[cost] + 1
    
print(-1)