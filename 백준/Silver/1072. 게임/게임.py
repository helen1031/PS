import sys
input = sys.stdin.readline

x, y = map(int, input().split())
z = y * 100 // x

left = 1
right = x
mincnt = sys.maxsize

while left <= right:
    mid = (left + right) // 2
    
    if (y + mid) * 100 // (x + mid) > z:
        mincnt = min(mincnt, mid)
        right = mid - 1
    else:
        left = mid + 1
        
if mincnt == sys.maxsize:
    print(-1)
else:
    print(mincnt)