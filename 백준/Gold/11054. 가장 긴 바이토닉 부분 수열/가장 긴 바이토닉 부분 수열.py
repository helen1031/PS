import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
ra = a[::-1]

upper = [1] * n
lower = [1] * n

for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]:
            upper[i] = max(upper[j] + 1, upper[i])
        if ra[j] < ra[i]:
            lower[i] = max(lower[j] + 1 , lower[i])

ans = 0
lower.reverse()
for i in range(n):
    ans = max(upper[i] + lower[i], ans)
print(ans-1)