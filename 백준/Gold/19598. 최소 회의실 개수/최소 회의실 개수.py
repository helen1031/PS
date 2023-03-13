import sys
input = sys.stdin.readline
import heapq

n = int(input())
hq = []
for _ in range(n):
    heapq.heappush(hq, list(map(int, input().split())))
    
rooms = [0]
while hq:
    sig = 0
    meeting = heapq.heappop(hq)
    for i, room in enumerate(rooms):
        if meeting[0] >= room:
            rooms[i] = meeting[1]
            sig = 1
            break
    if sig == 0:
        rooms.append(meeting[1])
        
print(len(rooms))