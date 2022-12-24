import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

jewelry = []
for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jewelry, (m, v))

bags = []
for _ in range(k):
    heapq.heappush(bags, int(input()))

total = 0
possible_gem = []

while bags:
    bag = heapq.heappop(bags)

    while jewelry and bag >= jewelry[0][0]:
        [gweight, gval] = heapq.heappop(jewelry)
        heapq.heappush(possible_gem, -gval)
    
    if possible_gem:
        total -= heapq.heappop(possible_gem)
    elif not jewelry:
        break
        
print(total)