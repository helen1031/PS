import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

dp = [[0] * (len(a)) for _ in range(len(b))]
if a[0] == b[0]:
    dp[0][0] = 1
    
for x in range(1, len(a)):
    dp[0][x] = dp[0][x-1]
    if a[x] == b[0]:
        dp[0][x] = 1
        
for y in range(1, len(b)):
    dp[y][0] = dp[y-1][0]
    if b[y] == a[0]:
        dp[y][0] = 1
        
        
for y in range(1, len(b)):
    for x in range(1, len(a)):
        dp[y][x] = dp[y-1][x-1]
        if b[y] == a[x]:
            dp[y][x] += 1
        dp[y][x] = max(dp[y][x], dp[y-1][x], dp[y][x-1])
            
print(dp[len(b)-1][len(a)-1])
        