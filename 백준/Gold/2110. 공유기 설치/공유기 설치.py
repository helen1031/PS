import sys

N, C = list(map(int, sys.stdin.readline().split()))

loc = []
for _ in range(N):
    loc.append(int(sys.stdin.readline()))
loc.sort()

left = 1
right = loc[-1] - loc[0]
res = 0

while(left <= right):
    mid = (left + right) // 2
    curr = loc[0]
    cnt = 1

    for i in range(1, N):
        if(curr + mid <= loc[i]) : # 공유기 설치위치 + 간격 <= 현재 탐색 좌표
            cnt += 1
            curr = loc[i]

    # 설치 더 필요 - 간격 좁혀야함
    if cnt < C :
        right = mid - 1

    # 간격 넓혀야 함
    else:
        left = mid + 1
        res = mid

print(res)