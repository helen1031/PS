import sys
input = sys.stdin.readline

def isSosu(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    
    a = n // 2
    b = n // 2
    
    while a > 0:
        if isSosu(a) and isSosu(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1
    