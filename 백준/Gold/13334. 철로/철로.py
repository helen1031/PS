import sys
input = sys.stdin.readline

import heapq

n = int(input())
info = [sorted(list(map(int, input().split()))) for _ in range(n)]
d = int(input())
# 어차피 d 넘어가는 선분은 포함될 수 없으니 처음부터 제거
distance = []
for i in info:
    if i[1] - i[0] <= d:
        distance.append(i)
distance.sort(key = lambda x:x[1])

candidate = []
cnt = 0
for dist in distance:
    # 최초 선분 삽입
    if not candidate:
        heapq.heappush(candidate, dist)
    else:
        # 철도 종료, 시작점 **(오른쪽 끝점을 기준으로 왼쪽방향으로 철로를 설정한다)**
        rail_e = dist[1]
        rail_s = rail_e - d
        # 철도에 포함이 안되면 후보군에서 박탈 - 최소heap의 시작좌표만 단순비교 하면 됨
        while len(candidate) > 0  and candidate[0][0] < rail_s:
            heapq.heappop(candidate)
        heapq.heappush(candidate, dist)
        cnt = max(cnt, len(candidate))

print(cnt)
