import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())
visited = [False] * 1000001

def bfs(start, stime):
    q = deque([(start, stime)])
    while q:
        now, time = q.popleft()

        if not visited[now]:
            visited[now] = True
            
            if now == k:
                return time

            if 0 <= now + 1 <= 100000:
                q.append((now + 1, time + 1))
            if 0 <= now - 1 <= 100000:
                q.append((now - 1, time + 1))
            if 0 <= now * 2 <= 100000:
                q.append((now * 2, time + 1))

    return time

print(bfs(n, 0))