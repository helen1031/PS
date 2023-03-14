import sys
input = sys.stdin.readline

n = int(input())
request = list(map(int, input().split()))
m = int(input())

request.sort()
left = 0
right = n-1
maxamnt = 0
while left <= right:
    div = right - left + 1
    limit = m // div
    if request[left] <= limit:
        m -= request[left]
        left += 1
    else:
        maxamnt = limit
        break
        
if maxamnt == 0:
    print(request[-1])
else:
    print(maxamnt)