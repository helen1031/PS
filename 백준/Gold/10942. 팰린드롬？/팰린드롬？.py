import sys
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))
m = int(input())

dp = [[0] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = 1

for d in range(1, n):
    for i in range(n-d):
        j = i + d
        if nlist[i] == nlist[j]:
            if j - i == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i+1][j-1]
                
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])