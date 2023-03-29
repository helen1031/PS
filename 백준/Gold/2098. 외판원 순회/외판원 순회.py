import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
ALL_VISIT = (1 << n) - 1

dp = [[None] * (1 << n) for _ in range(n)]
INF = int(1e9)

def dfs(last, visited):
    if visited == ALL_VISIT:
        return graph[last][0] or INF
    
    if dp[last][visited] is not None:
        return dp[last][visited]
    
    tmp = INF
    for city in range(n):
        if visited & (1 << city) == 0 and graph[last][city] != 0:
            tmp = min(tmp, dfs(city, visited | (1 << city)) + graph[last][city])
    dp[last][visited] = tmp
    return dp[last][visited]
    
print(dfs(0, 1 << 0))