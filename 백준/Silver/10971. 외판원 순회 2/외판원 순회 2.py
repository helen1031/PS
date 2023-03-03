import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
res = -1

def dfs(start, curr, cnt, total):
    global res
    
    if cnt == n:
        if cost[curr][start] != 0:
            total += cost[curr][start]
            if res == -1 or total < res:
                res = total
        return
    for i in range(n):
        if not visited[i] and cost[curr][i] != 0:
            visited[i] = True
            dfs(start, i, cnt + 1, total + cost[curr][i])
            visited[i] = False
    
for i in range(n):
    visited[i] = True
    dfs(i, i, 1, 0)
    visited[i] = False
    
print(res)