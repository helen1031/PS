import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(str, input().rstrip())) for _ in range(n)]

# 행 고정, x좌표 탐색
def colCnt():
    mcnt = 0
    for y in range(n):
        tmp = 1
        for x in range(n - 1):
            if board[y][x] == board[y][x+1]:
                tmp += 1
            else:
                tmp = 1
            mcnt = max(mcnt, tmp)

    return mcnt

# 열 고정, y좌표 탐색
def rowCnt():
    mcnt = 0
    for x in range(n):
        tmp = 1
        for y in range(n - 1):
            if board[y][x] == board[y+1][x]:
                tmp += 1
            else:
                tmp = 1
            mcnt = max(mcnt, tmp)

    return mcnt

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

maxcnt = 0
for y in range(n):
    for x in range(n):
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                # 인접 사탕이 서로 다르면
                if board[y][x] != board[ny][nx]:
                    board[y][x], board[ny][nx] = board[ny][nx], board[y][x]
                    maxcnt = max(maxcnt, rowCnt(), colCnt())
                    board[y][x], board[ny][nx] = board[ny][nx], board[y][x]

print(maxcnt)