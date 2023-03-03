n = int(input())
ans = 0
located = [0] * n

def check(y, x):
    # 놓인 열이 같거나 대각선에 있으면(기울기가 -1 or 1) False를 반환한다
    for j in range(y): # j는 행
        i = located[j] # i는 열
        if i == x or abs(i - x) == y - j:
            return False
    return True

def dfs(y):
    global ans
    if y == n:
        ans += 1
        return
    # cnt번째 행의 각 열을 돌면서(=각 행마다 퀸이 하나씩 놓여야 한다)
    # 놓을 수 있는 곳인지 검사한다
    # 놓을 수 있다면 dfs
    for x in range(n):
        located[y] = x # 열
        if check(y, x):
            dfs(y + 1)

dfs(0)
print(ans)