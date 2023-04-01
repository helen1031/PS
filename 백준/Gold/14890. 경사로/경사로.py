import sys
input = sys.stdin.readline

n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
installed = [[False] * n for _ in range(n)]

# 경사로 검사 방향
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def install(y, x, idx):
    for i in range(l):
        ny = y + dy[idx]
        nx = x + dx[idx]
        if 0 <= ny < n and 0 <= nx < n:
            installed[ny][nx] = True
            y, x = ny, nx


def isPossible(y, x, idx):
    height = graph[y][x]
    for i in range(l):
        ny = y + dy[idx]
        nx = x + dx[idx]
        if 0 <= ny < n and 0 <= nx < n and not installed[ny][nx] and height - 1 == graph[ny][nx]:
            y, x = ny, nx
        else:
            return False
    return True

cnt = 0

# 가로
for y in range(n):
    road = True
    height = graph[y][0]
    for x in range(1, n):
        if height == graph[y][x]:
            continue
        # 경사로 설치 방향 : / (높은 idx -> 낮은 idx)
        elif graph[y][x] - height == 1:
            if isPossible(y, x, 0):  # 높은 쪽 좌표 넘겨주기
                install(y, x, 0)
            else:
                road = False
                break
        # 경사로 설치 방향 : \ (낮은 idx -> 높은 idx)
        elif height - graph[y][x] == 1:
            if isPossible(y, x - 1, 1):
                install(y, x - 1, 1)
            else:
                road = False
                break
        else:
            road = False
            break
        height = graph[y][x]
    if road:
        cnt += 1

installed = [[False] * n for _ in range(n)]
# 세로
for x in range(n):
    road = True
    height = graph[0][x]
    for y in range(1, n):
        if height == graph[y][x]:
            continue
        # 경사로 설치 방향: 높은 idx -> 낮은 idx
        elif graph[y][x] - height == 1:
            if isPossible(y, x, 2):
                install(y, x, 2)
            else:
                road = False
                break
        elif height - graph[y][x] == 1:
            if isPossible(y - 1, x, 3):
                install(y - 1, x, 3)
            else:
                road = False
                break
        else:
            road = False
            break
        height = graph[y][x]

    if road:
        cnt += 1

print(cnt)