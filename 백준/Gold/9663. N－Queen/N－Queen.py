n = int(input())

col = [0] * n
rowCheck = [False] * n
diag1Check = [False] * (2 * n - 1)
diag2Check = [False] * (2 * n - 1)
ans = 0

def set(x):
	global ans

	for y in range(n):
		if not rowCheck[y] and not diag1Check[x + y] and not diag2Check[x - y + n - 1]:
			col[x] = y
			if x == n - 1:
				ans += 1
			else:
				rowCheck[y] = diag1Check[x+y] = diag2Check[x-y+n-1] = True
				set(x+1)
				rowCheck[y] = diag1Check[x+y] = diag2Check[x-y+n-1] = False
                
set(0)
print(ans)