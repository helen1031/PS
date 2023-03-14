import sys
input = sys.stdin.readline

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
points.append(points[0])

xsum = 0
ysum = 0
for i in range(n):
    xsum += points[i][0] * points[i+1][1]
    ysum += points[i][1] * points[i+1][0]
    
print(round(abs((xsum - ysum) / 2), 1))