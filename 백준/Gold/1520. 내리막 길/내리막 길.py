import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n = map(int, input().split())
height = [list(map(int, input().split())) for _ in range(m)]

dp = [[None] * n for _ in range(m)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(y, x):
    if y == m - 1 and x == n - 1:
        return 1
    
    if dp[y][x] is not None:
        return dp[y][x]
    
    tmp = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < m and 0 <= nx < n and height[ny][nx] < height[y][x]:
            tmp += dfs(ny, nx)
    dp[y][x] = tmp
    return dp[y][x]
            
print(dfs(0, 0))