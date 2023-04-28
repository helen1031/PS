import sys
input = sys.stdin.readline

n = int(input())
honeys = list(map(int, input().split()))

maxsum = 0

sum = [honeys[0]]
for i in range(1, n):
    sum.append(sum[i-1] + honeys[i])

# 벌통 맨 오른쪽
for i in range(1, n-1):
    bee1 = sum[n-1] - honeys[0] - honeys[i]
    bee2 = sum[n-1] - sum[i]
    maxsum = max(maxsum, bee1 + bee2)

# 벌통 맨 왼쪽
for i in range(1, n-1):
    bee1 = sum[n-2] - honeys[i]
    bee2 = sum[i-1]
    maxsum = max(maxsum, bee1 + bee2)

# 벌통 중간
for i in range(1, n-1):
    bee1 = sum[i] - honeys[0]
    bee2 = sum[n-2] - sum[i] + honeys[i]
    maxsum = max(maxsum, bee1 + bee2)

print(maxsum)