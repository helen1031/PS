from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
board = [[0] * n for _ in range(n)]
board[0][0] = 2

for _ in range(int(input())):
    y, x = map(int, input().split())
    board[y-1][x-1] = 1

l = int(input())
moves = {}
for _ in range(l):
    x, c = map(str, input().strip().split())
    moves[int(x)] = c

time = 0

dy = [0, 1, 0, -1]  # RDLU
dx = [1, 0, -1, 0]
dir = 0

cy, cx = 0, 0
snake = deque()
snake.append((0, 0))
while True:
    ny, nx = cy + dy[dir], cx + dx[dir]
    time += 1

    if 0 > ny or ny >= n or 0 > nx or nx >= n:
        break

    if board[ny][nx] == 2:
        break

    elif board[ny][nx] == 1:
        board[ny][nx] = 2

    else:
        board[ny][nx] = 2
        ty, tx = snake.popleft()
        board[ty][tx] = 0

    if time in moves:
        if moves[time] == 'D':
            dir = (dir + 1) % 4
        else:
            dir = (dir - 1) % 4

    cy, cx = ny, nx
    snake.append((cy, cx))

print(time)
