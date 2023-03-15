import sys
input = sys.stdin.readline

import heapq

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
info.sort(key = lambda x:x[0])

hq = []
for i in info:
    deadline, food = i[0], i[1]
    heapq.heappush(hq, food)
    if len(hq) > deadline:
        heapq.heappop(hq)
        
print(sum(hq))