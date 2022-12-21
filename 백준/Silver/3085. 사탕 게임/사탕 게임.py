from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
board = [list(input().strip()) for _ in range(n)]


def count():
    maxx = 0
    for i in range(n):
        xcnt = 1
        for j in range(n-1):
            if board[i][j] == board[i][j+1]:
                xcnt += 1
            else:
                xcnt = 1
            maxx = max(maxx, xcnt)

    maxy = 0
    for i in range(n):
        ycnt = 1
        for j in range(n-1):
            if board[j][i] == board[j+1][i]:
                ycnt += 1
            else:
                ycnt = 1
            maxy = max(maxy, ycnt)

    return max(maxx, maxy)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

cnt = 0
for y in range(n):
    for x in range(n):
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if board[y][x] != board[ny][nx]:
                    board[y][x], board[ny][nx] = board[ny][nx], board[y][x]
                    cnt = max(cnt, count())
                    board[y][x], board[ny][nx] = board[ny][nx], board[y][x]

print(cnt)