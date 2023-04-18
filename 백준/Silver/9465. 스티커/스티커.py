import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    dp = [list(map(int, input().split())), list(map(int, input().split()))]

    if n > 1:
        dp[0][1] = dp[1][0] + dp[0][1]
        dp[1][1] = dp[0][0] + dp[1][1]

        for i in range(2, n):
            dp[0][i] = max(dp[1][i-1] + dp[0][i], dp[1][i-2] + dp[0][i])
            dp[1][i] = max(dp[0][i-1] + dp[1][i], dp[0][i-2] + dp[1][i])
            
    print(max(dp[0][-1], dp[1][-1]))