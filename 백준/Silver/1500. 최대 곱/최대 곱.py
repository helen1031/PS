s, k = map(int, input().split())

n = s // k
nums = [n for _ in range(k)]
s -= n * k

for i in range(s):
    nums[i] += 1
    
res = 1
for num in nums:
    res *= num
print(res)