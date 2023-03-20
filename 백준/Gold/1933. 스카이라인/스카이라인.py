import sys
input = sys.stdin.readline

import heapq

n = int(input())
buildings = []
for i in range(n):
    l, h, r = map(int, input().split())
    buildings.append([l, h, r])
    buildings.append([r, 0, r])

buildings.sort(key = lambda x: (x[0], -x[1]))

hq = []
ans = []
current = 0
for building in buildings:
    left, height, right = building[0], building[1], building[2]
    # 건물 시작 정보라면
    if left != right:
        # 건물 높이보다 현재 탐색 위치 높이가 더 높다면 - 정답 기록
        if current < height:
            current = height
            ans.append([left, height])
        heapq.heappush(hq, [-height, left, right])

    # 건물 끝 정보라면
    else:
        # 현 최대 높이 건물 끝 지점보다 이전에 마무리 된 좌표라면- 그냥 무시
        # 현 최대 높이 건물 끝 지점이랑 같거나 이후에 마무리된 좌표라면 - ans 기록, pop
        if hq and left >= hq[0][2]:
            while hq and left >= hq[0][2]:
                heapq.heappop(hq)
            if hq:
                if -hq[0][0] != current:
                    current = -hq[0][0]
                    ans.append([left, -hq[0][0]])
            else:
                current = 0
                ans.append([left, height])
        else:
            continue
for i in ans:
    print(i[0], i[1], end=" ")