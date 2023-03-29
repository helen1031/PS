import sys
input = sys.stdin.readline

n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

def dfs(y, x, direction):
    global cnt
    
    if y == x == n - 1:
        cnt += 1
        return
    # 가로, 세로, 대각선 -> 대각선 이동
    if y + 1 < n and x + 1 < n:
        if house[y][x+1] == 0 and house[y+1][x] == 0 and house[y+1][x+1] == 0:
            dfs(y+1, x+1, 2)
    
    # 세로, 대각선 -> 세로 이동
    if direction == 1 or direction == 2:
        if y + 1 < n and house[y+1][x] == 0:
            dfs(y+1, x, 1)
    
    # 가로, 대각선 -> 가로 이동
    if direction == 0 or direction == 2:
        if x + 1 < n and house[y][x+1] == 0:
            dfs(y, x+1, 0)
            
dfs(0, 1, 0) # 방향 - 0 가로, 1 세로, 2 대각선
print(cnt)