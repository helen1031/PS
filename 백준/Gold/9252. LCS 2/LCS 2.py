import sys
input = sys.stdin.readline

x = ' ' + input().rstrip()
y = ' ' + input().rstrip()

dp = [[0] * len(y) for _ in range(len(x))]

for i in range(1, len(x)):
    for j in range(1, len(y)):
        if x[i] == y[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
print(dp[-1][-1])

if dp[-1][-1] != 0:
    lcs = ""
    i = len(x)-1
    j = len(y)-1
    while len(lcs) < dp[-1][-1]:
        if x[i] == y[j]:
            lcs = x[i] + lcs
            i -= 1
            j -= 1
        else:
            if dp[i][j] == dp[i-1][j]:
                i -= 1
            else:
                j -= 1
    print(lcs)