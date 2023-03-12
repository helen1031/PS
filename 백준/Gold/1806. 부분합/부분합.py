n, s = map(int, input().split())
nums = list(map(int, input().split()))

ans = 100000001
left = 0
right = 0
partial = 0
length = 0

while True:
    if partial >= s:
        ans = min(ans, length)
        partial -= nums[left]
        left += 1
        length -= 1
    elif right == n:
        break
    else:
        partial += nums[right]
        right += 1
        length += 1
    
if ans == 100000001:
    ans = 0
print(ans)