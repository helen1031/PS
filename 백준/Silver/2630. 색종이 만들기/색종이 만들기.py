import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split(" "))) for _ in range(n)]
white = 0
blue = 0

def colorChk(sy, sx, length, color):
    for y in range(length):
        for x in range(length):
            if paper[sy+y][sx+x] != color:
                return False
    return True

def colorCng(sy, sx, length):
    for y in range(length):
        for x in range(length):
            paper[sy+y][sx+x] = -1

length = n
while length > 0:
    for y in range(0, n, length):
        for x in range(0, n, length):
            color = paper[y][x]
            if color == -1:
                continue

            if colorChk(y, x, length, color):
                if color == 1:
                    blue += 1
                else:
                    white += 1
                colorCng(y, x, length)
    length = length // 2

print(white)
print(blue)