from collections import deque
import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
devices = deque(list(map(str, input().rstrip().split())))

use = []
while len(use) < n and devices:
    cur = devices.popleft()
    hit = 0
    for u in use:
        if u == cur:
            hit = 1
            break
    if hit == 0:
        use.append(cur)

plug = 0
while devices:
    nextd = devices.popleft()
    hit = 0
    score = []

    if len(use) < n:
        use.append(nextd)
        continue

    for u in use:
        idx = ''.join(devices).find(str(u))
        if idx == -1:
            idx = k
        heapq.heappush(score, (-idx, u))
        if u == nextd:
            hit = 1
            break

    if hit == 0:
        selected = heapq.heappop(score)
        plug += 1
        use.remove(selected[1])
        use.append(nextd)
    else:
        continue

print(plug)