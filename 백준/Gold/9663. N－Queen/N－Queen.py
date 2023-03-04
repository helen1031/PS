n = int(input())
info = [0] * n
located = [False] * n
diag1 = [False] * (2 * n-1)
diag2 = [False] * (2 * n-1)
ans = 0

def set(i):
    global ans
    for j in range(n):
        if not located[j] and not diag1[i+j] and not diag2[i-j+ n -1]:
            info[i] = j
            if i == n - 1:
                ans += 1
            else:
                located[j] = diag1[i+j] = diag2[i-j+ n -1] = True
                set(i+1)
                located[j] = diag1[i+j] = diag2[i-j+ n -1] = False
    
set(0)
print(ans)