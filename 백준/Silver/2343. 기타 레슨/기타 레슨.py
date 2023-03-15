import sys, math
input = sys.stdin.readline

n, m = map(int, input().split())
lectures = list(map(int, input().split()))

left = max(lectures)
right = sum(lectures)

while left <= right:
    mid = (left + right) // 2
    cnt = 1
    tmp = 0
    for lecture in lectures:
        if tmp + lecture <= mid:
            tmp += lecture
        else:
            cnt += 1
            tmp = lecture
        if cnt > m:
            break
    
    if cnt <= m:
        right = mid - 1
    else:
        left = mid + 1
        
print(left)
