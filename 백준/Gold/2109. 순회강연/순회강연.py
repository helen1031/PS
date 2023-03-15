import sys
input = sys.stdin.readline

import heapq

n = int(input())
lectures = [list(map(int, input().split())) for _ in range(n)]
lectures.sort(key = lambda x: x[1]) # 날짜기준 정렬

hq = []

for lecture in lectures:
    price, day = lecture[0], lecture[1]
    heapq.heappush(hq, price)
    if len(hq) > day:
        heapq.heappop(hq)
        
print(sum(hq))               
              