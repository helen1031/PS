import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

res = 0
l = 0
r = max(trees)
while l <= r:
    h = (l+r) // 2
    cut = sum([t - h if t > h else 0 for t in trees])
    
    if cut == m:
        res = h
        break
    # 더 많이 잘려서 높이를 높여야 됨
    elif cut > m:
        res = h
        l = h + 1
    # 덜 잘려서 높이를 낮춰야 됨
    else:
        r = h -1
        
print(res)