from collections import deque
import copy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]
camera = deque()
safeZone = n * m
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
dir = {1: [[0], [1], [2], [3]], 
       2: [[0, 2], [1, 3]], 
       3: [[0, 1], [1, 2], [2, 3], [3, 0]], 
       4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
       5: [[0, 1, 2, 3]]}

def count_area(coffice):
    tmp = 0
    for y in range(n):
        for x in range(m):
            if coffice[y][x] == 0:
                tmp += 1
    return tmp

def detect_area(y, x, direction, coffice):
    for d in direction:
        ny, nx = y, x
        while True:
            ny += dy[d]
            nx += dx[d]
            if 0 <= ny < n and 0 <= nx < m:
                if coffice[ny][nx] == 0:
                    coffice[ny][nx] = '#'
                elif coffice[ny][nx] == 6:
                    break
            else:
                break

def dfs(idx, office):
    copy_office = copy.deepcopy(office)
    
    if idx == len(camera):
        global safeZone
        safeZone = min(count_area(copy_office), safeZone)
        return
    
    y, x, cam = camera[idx]
    for d in dir[cam]:
        detect_area(y, x, d, copy_office)
        dfs(idx+1, copy_office)
        copy_office = copy.deepcopy(office)
            


for y in range(n):
    for x in range(m):
        if 1 <= office[y][x] <= 5:
            camera.append((y, x, office[y][x]))
    
dfs(0, office)
print(safeZone)