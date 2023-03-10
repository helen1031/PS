a, b, c = map(int, input().split())

def cal(n):
    if n == 1:
        return a % c
    
    
    if n % 2 == 0:
        return cal(n//2) ** 2 % c
    else:
        return cal(n//2) ** 2 * a % c

print(cal(b))