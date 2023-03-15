import sys
input = sys.stdin.readline

import heapq

n, m = map(int, input().split())
cards = []
for card in map(int, input().split()):
    heapq.heappush(cards, card)

for _ in range(m):
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)
    heapq.heappush(cards, x+y)
    heapq.heappush(cards, x+y)
    
print(sum(cards))