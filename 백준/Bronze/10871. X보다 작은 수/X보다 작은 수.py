import sys
input = sys.stdin.readline

n, x = map(int, input().split())
nums = list(map(int, input().split()))
snum = []
for num in nums:
    if num < x :
        snum.append(num)
        
print(*snum)