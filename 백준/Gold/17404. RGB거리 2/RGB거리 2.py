import sys
input = sys.stdin.readline

INF = int(1e9)
n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

answer = INF
for color in range(3) : # R,G,B
    dp = [[INF] * 3 for _ in range(n)]
    dp[0][color] = cost[0][color] # 최초 집에 색깔 칠하기
    for i in range(1, n):
        dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])
    for last in range(3): # 최초 집과 마지막 집 색깔이 같지 않은 케이스만 고려
        if color != last:
            answer = min(answer, dp[-1][last])
            
print(answer)