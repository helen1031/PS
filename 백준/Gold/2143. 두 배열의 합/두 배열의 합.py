import sys
input = sys.stdin.readline
from collections import defaultdict

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

sumA = {}
sumA = defaultdict(int)
for i in range(n):
    for j in range(i, n):
        sumA[sum(a[i:j+1])] += 1
ans = 0
for i in range(m):
    for j in range(i, m):
        ans += sumA[t - sum(b[i:j+1])]

print(ans)