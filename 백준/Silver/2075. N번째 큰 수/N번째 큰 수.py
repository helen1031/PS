import sys
input = sys.stdin.readline

import heapq

n = int(input())
hq = []

for _ in range(n):
    for num in map(int, input().split()):
        if len(hq) < n:
            heapq.heappush(hq, num)
        else:
            heapq.heappush(hq, num)
            heapq.heappop(hq)

print(hq[0])