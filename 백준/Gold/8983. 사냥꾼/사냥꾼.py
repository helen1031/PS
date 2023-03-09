import sys
input = sys.stdin.readline

m, n, l = map(int, input().split())
shootpos = list(map(int, input().split()))
shootpos.sort()
anipos = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for a, b in anipos:
    if b > l :
        continue
    # 동물을 잡을 수 있는 사대 좌표 범위
    minpos = a + b - l
    maxpos = a - b + l
    left = 0
    right = m -1
    while left <= right:
        mid = (left + right) // 2
        if minpos <= shootpos[mid] <= maxpos:
            cnt += 1
            break
        else:
            # minpos 가 mid 보다 크면
            if shootpos[mid] < maxpos:
                left = mid + 1
            # maxpos 가 mid보다 작으면
            else:
                right = mid - 1
        
print(cnt)
            