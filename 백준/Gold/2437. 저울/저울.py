n = int(input())
weight = list(map(int, input().split()))
weight.sort()

ans = 0
for i in range(n):
    if ans + 1 >= weight[i]:
        ans += weight[i]
    else:
        break
print(ans+1)