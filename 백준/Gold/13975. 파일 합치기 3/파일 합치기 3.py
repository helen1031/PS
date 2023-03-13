import sys
input = sys.stdin.readline

import heapq

t = int(input())
for _ in range(t):
    k = int(input())
    papers = list(map(int, input().split()))
    hq = []
    ans = 0
    for paper in papers:
        heapq.heappush(hq, paper)
    while len(hq) > 1:
        a = heapq.heappop(hq)
        b = heapq.heappop(hq)
        ans += a + b
        heapq.heappush(hq, a+b)
    print(ans)
        