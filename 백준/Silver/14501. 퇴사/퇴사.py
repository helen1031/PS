import sys
input = sys.stdin.readline

n = int(input())
information = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n + 1)
mcost = 0

# 날짜 역순 탐색
for d in range(n-1, -1, -1):
    day, cost = information[d]
    # 퇴사일 초과
    if d + day > n:
        dp[d] = mcost
    # 퇴사일 이내
    else:
        dp[d] = max(dp[d + day] + cost, mcost)
        mcost = dp[d]
        
print(dp[0])
