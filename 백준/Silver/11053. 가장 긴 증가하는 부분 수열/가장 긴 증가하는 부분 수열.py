import sys
input = sys.stdin.readline

n = int(input())
nl = list(map(int, input().split()))
dp = [nl[0]]

for i in range(1, n):
    if dp[-1] < nl[i]:
        dp.append(nl[i])
    else:
        x = len(dp) - 1
        while x > 0:
            if dp[x-1] < nl[i]:
                break
            x -= 1
        dp[x] = nl[i]
print(len(dp))