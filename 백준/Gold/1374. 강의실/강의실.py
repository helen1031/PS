import sys
input = sys.stdin.readline
import heapq

n = int(input())
hq = []
for _ in range(n):
    no, start, end = map(int, input().split())
    heapq.heappush(hq, [start, end])
    
classrooms = [0]
while hq:
    sig = 0
    current = heapq.heappop(hq)
    for i, classroom in enumerate(classrooms):
        if classroom <= current[0]:
            classrooms[i] = current[1]
            sig = 1
            break
    if sig == 0:
        classrooms.append(current[1])
            

print(len(classrooms))