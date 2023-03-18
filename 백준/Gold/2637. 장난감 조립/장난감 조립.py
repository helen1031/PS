import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
dp = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    x, y, k = map(int, input().split())
    graph[y].append((x, k))
    indegree[x] += 1

q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()

    for i in graph[now]:
        prod, cnt = i

        if dp[now].count(0) == n + 1:
            # 기본 구성품이라면
            dp[prod][now] += cnt
        else:
            # 중간 구성품이라면
            for i in range(1, n+1):
                dp[prod][i] += dp[now][i] * cnt

        indegree[prod] -= 1
        if indegree[prod] == 0:
            q.append(prod)

for i, cnt in enumerate(dp[n][1:]):
    if cnt > 0:
        print(i+1, cnt)
