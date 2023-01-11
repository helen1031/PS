import sys
input = sys.stdin.readline

gears = [list(input().rstrip()) for _ in range(4)]
gears = [0] + gears

for _ in range(int(input())):
    num, dir = map(int, input().split())
    spin = [0, 0, 0, 0, 0]
    spin[num] = dir
    for i in range(num+1, 5):
        if spin[i-1] == 0:
            continue
        if gears[i-1][2] != gears[i][6]:
            spin[i] = -1 * spin[i-1]
            
    for i in range(num-1, 0, -1):
        if spin[i+1] == 0:
            continue
        if gears[i+1][6] != gears[i][2]:
            spin[i] = -1 * spin[i+1]
            
    for i in range(1, 5):
        if spin[i] == 1:
            gears[i] = (gears[i] + gears[i])[7:-1]
        elif spin[i] == -1:
            gears[i] = (gears[i] + gears[i])[1:9]

score = 0
            
if gears[1][0] == "1":
    score += 1
if gears[2][0] == "1":
    score += 2
if gears[3][0] == "1":
    score += 4
if gears[4][0] == "1":
    score += 8
    
print(score)