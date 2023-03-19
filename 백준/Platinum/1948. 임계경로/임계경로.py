import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

from collections import deque

n = int(input())
m = int(input())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
graph_r = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph_r[b].append((a, c))
    indegree[b] += 1
start, end = map(int, input().split())

costs = [0] * (n + 1)

def topology():
    q = deque()
    q.append((start, 0))
    while q:
        now, cost = q.popleft()

        for i in graph[now]:
            next, ncost = i
            indegree[next] -= 1
            tmpcost = cost + ncost
            costs[next] = max(costs[next], tmpcost)

            if indegree[next] == 0:
                q.append((next, costs[next]))

visited = [False] * (n + 1)
costs_r= [0] * (n + 1)
critical = 0
def dfs(now, cost):
    global critical

    if visited[now]:
        return

    visited[now] = True
    for i in graph_r[now]:
        next, ncost = i
        tmpcost = cost - ncost
        if tmpcost == costs[next]:
            critical += 1
            dfs(next, tmpcost)

topology()
print(costs[end])
dfs(end, costs[end])
print(critical)
