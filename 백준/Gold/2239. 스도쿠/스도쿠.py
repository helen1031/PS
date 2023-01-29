import sys
input = sys.stdin.readline

sudoku = [list(map(int, input().rstrip())) for _ in range(9)]
blank = []

def check(num, y, x):
    for row in range(9):
        if num == sudoku[row][x]:
            return False

    for col in range(9):
        if num == sudoku[y][col]:
            return False

    sy = (y // 3) * 3
    sx = (x // 3) * 3
    for row in range(3):
        for col in range(3):
            if num == sudoku[sy+row][sx+col]:
                return False

    return True

def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(''.join(map(str, sudoku[i])))
        exit()
    y, x = blank[idx]
    for n in range(1, 10):
        if check(n, y, x):
            sudoku[y][x] = n
            dfs(idx + 1)
            sudoku[y][x] = 0

for y in range(9):
    for x in range(9):
        if sudoku[y][x] == 0:
            blank.append((y, x))

dfs(0)