import sys
input = sys.stdin.readline

import heapq

n = int(input())
homeworks = [list(map(int, input().split())) for _ in range(n)]
homeworks.sort(key = lambda x:x[0])

hq = []
for homework in homeworks:
    d, w = homework[0], homework[1]
    heapq.heappush(hq, w)
    if len(hq) > d:
        heapq.heappop(hq)
        
print(sum(hq))