import sys
input = sys.stdin.readline

n = int(input())
image = [list(input()) for _ in range(n)]
res = ""

def colorChk(sy, sx, length):
    global res
    color = image[sy][sx]
    for y in range(sy, sy+length):
        for x in range(sx, sx+length):
            if image[y][x] != color:
                res += "("
                colorChk(sy, sx, length // 2)
                colorChk(sy, sx + length // 2, length // 2)
                colorChk(sy + length // 2, sx, length // 2)
                colorChk(sy + length // 2, sx+ length // 2, length // 2)
                res += ")"
                return
    res += color
    return color

colorChk(0, 0, n)
print(res)