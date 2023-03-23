import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())
visited = [-1] * 1000001
def bfs(start):
    q = deque([start])
    visited[start] = 0

    while q:
        now = q.popleft()

        if now == k:
            return

        for nxt in (now + 1, now - 1, now * 2):
            if 0 <= nxt <= 100000 and visited[nxt] == -1:
                q.append(nxt)
                visited[nxt] = visited[now] + 1

bfs(n)
print(visited[k])