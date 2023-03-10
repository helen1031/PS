import sys
import heapq

N = int(sys.stdin.readline())
heap = []
for i in range(N):
    heapq.heappush(heap, int(sys.stdin.readline()))

result = 0

while len(heap) != 1:
    first, second = heapq.heappop(heap), heapq.heappop(heap)
    new = first + second
    heapq.heappush(heap, new)
    result += new

print(result)