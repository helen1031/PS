import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())
visited = [-1] * 100001
cnt = 0

def bfs(start):
    global cnt

    q = deque([start])
    visited[start] = 0

    while q:
        now = q.popleft()

        if now == k:
            cnt += 1

        if 0 <= now + 1 <= 100000 and (visited[now + 1] == -1 or visited[now + 1] == visited[now] + 1):
            q.append(now + 1)
            visited[now + 1] = visited[now] + 1
        if 0 <= now - 1 <= 100000 and (visited[now - 1] == -1 or visited[now - 1] == visited[now] + 1):
            q.append(now - 1)
            visited[now - 1] = visited[now] + 1
        if 0 <= now * 2 <= 100000 and (visited[now * 2] == -1 or visited[now * 2] == visited[now] + 1):
            q.append(now * 2)
            visited[now * 2] = visited[now] + 1

bfs(n)
print(visited[k])
print(cnt)