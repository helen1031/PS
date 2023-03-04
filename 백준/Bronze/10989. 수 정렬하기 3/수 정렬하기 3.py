import sys
input = sys.stdin.readline

n = int(input())
nums = [0] * 10001
for _ in range(n):
    nums[int(input())] += 1
    
for i in range(1, 10001):
    cnt = nums[i]
    for j in range(cnt):
        print(i)