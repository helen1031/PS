import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split())) # + - * /

mincal = 1000000001
maxcal = -1000000001
def dfs(num, cnt, add, sub, mul, div):
    global mincal, maxcal
    
    if cnt == n:
        if num < mincal:
            mincal = num
        if num > maxcal:
            maxcal = num
        return
    
    if add > 0:
        dfs(num + nums[cnt], cnt + 1, add-1, sub, mul, div)
    if sub > 0:
        dfs(num - nums[cnt], cnt + 1, add, sub-1, mul, div)
    if mul > 0:
        dfs(num * nums[cnt], cnt + 1, add, sub, mul-1, div)
    if div > 0:
        dfs(int(num / nums[cnt]), cnt + 1, add, sub, mul, div-1)
    
    
dfs(nums[0], 1, ops[0], ops[1], ops[2], ops[3])
print(maxcal)
print(mincal)