import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
cards.sort()

m = int(input())
nums = list(map(int, input().split()))
ans = [0] * m
for i, num in enumerate(nums):
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if num == cards[mid]:
            ans[i] = 1
            break
        elif num > cards[mid]:
            left = mid + 1
        else:
            right = mid - 1
print(*ans)