from copy import deepcopy
import sys
input = sys.stdin.readline

n = int(input())
init = [list(map(int, input().split())) for _ in range(n)]
ans = 0


def collision(dir, board):
    if dir == 0:  # 상
        for x in range(n):
            ypoint = 0
            for y in range(1, n):
                if board[y][x]:
                    tmp = board[y][x]
                    board[y][x] = 0

                    if board[ypoint][x] == 0:
                        board[ypoint][x] = tmp
                    elif board[ypoint][x] == tmp:
                        board[ypoint][x] *= 2
                        ypoint += 1
                    else:
                        ypoint += 1
                        board[ypoint][x] = tmp

    elif dir == 1:  # 하
        for x in range(n):
            ypoint = n - 1
            for y in range(n - 2, -1, -1):
                if board[y][x]:
                    tmp = board[y][x]
                    board[y][x] = 0

                    if board[ypoint][x] == 0:
                        board[ypoint][x] = tmp
                    elif board[ypoint][x] == tmp:
                        board[ypoint][x] *= 2
                        ypoint -= 1
                    else:
                        ypoint -= 1
                        board[ypoint][x] = tmp

    elif dir == 2:  # 좌
        for y in range(n):
            xpoint = 0
            for x in range(1, n):
                if board[y][x]:
                    tmp = board[y][x]
                    board[y][x] = 0

                    if board[y][xpoint] == 0:
                        board[y][xpoint] = tmp
                    elif board[y][xpoint] == tmp:
                        board[y][xpoint] *= 2
                        xpoint += 1
                    else:
                        xpoint += 1
                        board[y][xpoint] = tmp

    else:  # 우
        for y in range(n):
            xpoint = n - 1
            for x in range(xpoint - 1, -1, -1):
                if board[y][x]:
                    tmp = board[y][x]
                    board[y][x] = 0

                    if board[y][xpoint] == 0:
                        board[y][xpoint] = tmp
                    elif board[y][xpoint] == tmp:
                        board[y][xpoint] *= 2
                        xpoint -= 1
                    else:
                        xpoint -= 1
                        board[y][xpoint] = tmp
    return board

def move(board, cnt):
    global ans
    if cnt == 5:
        for b in board:
            ans = max(ans, max(b))
        return

    for i in range(4):
        nboard = collision(i, deepcopy(board))
        move(nboard, cnt + 1)


move(init, 0)
print(ans)


