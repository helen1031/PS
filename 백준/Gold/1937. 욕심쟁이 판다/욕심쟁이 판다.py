import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n + 1)]
def dfs(y, x):

    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if graph[y][x] < graph[ny][nx]:
                dp[y][x] = max(dp[y][x], dfs(ny, nx) + 1)

    return dp[y][x]

ans = 0
for y in range(n):
    for x in range(n):

        ans = max(ans, dfs(y, x))
print(ans)