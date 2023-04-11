import sys
input = sys.stdin.readline

INF = int(1e9)


n, s = map(int, input().split())
nums = list(map(int, input().split()))
part = nums[0]
ans = INF

left, right = 0, 0

while True:
    if part >= s:
        ans = min(ans, right - left + 1)
        part -= nums[left]
        left += 1

    elif right == n -1:
        break

    else:
        right += 1
        part += nums[right]

print(0) if ans == INF else print(ans)
