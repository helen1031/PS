import sys
input = sys.stdin.readline

import heapq

q = []
for _ in range(int(input())):
    op = int(input())
    if op == 0:
        if len(q) == 0 :
            print(0)
        else:
            print(-1 * heapq.heappop(q))
    else:
        heapq.heappush(q, -op)