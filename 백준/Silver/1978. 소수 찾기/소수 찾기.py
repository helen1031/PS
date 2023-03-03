import sys
input = sys.stdin.readline

def sosu(num):
    if num == 1:
        return False
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True

n = int(input())
nums = list(map(int, input().split()))

cnt = 0
for i in range(n):
    num = nums[i]
    if sosu(num):
        cnt += 1
print(cnt)