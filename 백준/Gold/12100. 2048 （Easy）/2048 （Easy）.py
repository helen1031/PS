import sys
input = sys.stdin.readline

import copy

n = int(input())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

mblock = 0
game = [list(map(int, input().split())) for _ in range(n)]

def collision(gcopy, dir):
    if dir == 0:  # 상
        for x in range(n):
            ypoint = 0
            for y in range(1, n):
                if gcopy[y][x]:
                    tmp = gcopy[y][x]
                    gcopy[y][x] = 0

                    if gcopy[ypoint][x] == 0:
                        gcopy[ypoint][x] = tmp
                    elif gcopy[ypoint][x] == tmp:
                        gcopy[ypoint][x] *= 2
                        ypoint += 1
                    else:
                        ypoint += 1
                        gcopy[ypoint][x] = tmp

    elif dir == 1:
        for x in range(n):
            ypoint = n - 1
            for y in range(n-2, -1, -1):
                if gcopy[y][x]:
                    tmp = gcopy[y][x]
                    gcopy[y][x] = 0

                    if gcopy[ypoint][x] == 0:
                        gcopy[ypoint][x] = tmp
                    elif gcopy[ypoint][x] == tmp:
                        gcopy[ypoint][x] *= 2
                        ypoint -= 1

                    else:
                        ypoint -= 1
                        gcopy[ypoint][x] = tmp
    elif dir == 2:
        for y in range(n):
            xpoint = 0
            for x in range(1, n):
                if gcopy[y][x]:
                    tmp = gcopy[y][x]
                    gcopy[y][x] = 0

                    if gcopy[y][xpoint] == 0:
                        gcopy[y][xpoint] = tmp
                    elif gcopy[y][xpoint] == tmp:
                        gcopy[y][xpoint] *= 2
                        xpoint += 1
                    else:
                        xpoint += 1
                        gcopy[y][xpoint] = tmp
    else:
        for y in range(n):
            xpoint = n - 1
            for x in range(n-2, -1, -1):
                if gcopy[y][x]:
                    tmp = gcopy[y][x]
                    gcopy[y][x] = 0

                    if gcopy[y][xpoint] == 0:
                        gcopy[y][xpoint] = tmp
                    elif gcopy[y][xpoint] == tmp:
                        gcopy[y][xpoint] *= 2
                        xpoint -= 1
                    else:
                        xpoint -= 1
                        gcopy[y][xpoint] = tmp
    return gcopy

def move(game, mcnt):
    global mblock
    if mcnt == 5:
        for g in game:
            mblock = max(mblock, max(g))
        return

    for i in range(4):
        gcopy = collision(copy.deepcopy(game), i)
        # for g in gcopy:
        #     print(*g)
        # print("-------")
        move(gcopy, mcnt + 1)

move(game, 0)
print(mblock)