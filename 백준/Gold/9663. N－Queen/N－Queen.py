n = int(input())
ypos = [0] * n
xpos = [False] * n
diag1 = [False] * (2 * n -1)
diag2 = [False] * (2 * n -1)
ans = 0

def dfs(y):
    global ans
    
    for x in range(n):
        if not xpos[x] and not diag1[y + x] and not diag2[n - y + x - 1]:
            ypos[y] = x 
            if y == n-1:
                ans+= 1
            else:
                xpos[x] = diag1[y+x] = diag2[n-y+x-1] = True
                dfs(y+1)
                xpos[x] = diag1[y+x] = diag2[n-y+x-1] = False
    
dfs(0)
print(ans)