import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

INF = int(1e9)
answer = INF
for color in range(3):
    dp = [[INF] * 3 for _ in range(n)]
    dp[0][color] = cost[0][color]
    
    for i in range(1, n):
        dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])
        
    answer = min(answer, min(dp[-1]))
print(answer)