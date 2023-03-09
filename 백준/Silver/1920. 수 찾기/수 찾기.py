import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
comp = list(map(int, input().split()))

for c in comp:
    pl = 0
    pr = n - 1
    while True:
        pc = (pl + pr) // 2
        if c == a[pc]:
            print(1)
            break
        elif c < a[pc]:
            pr = pc - 1
        else:
            pl = pc + 1
            
        if pl > pr:
            print(0)
            break