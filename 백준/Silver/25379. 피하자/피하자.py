import sys
input = sys.stdin.readline

n = int(input())
alist = list(map(int, input().split()))

for i, a in enumerate(alist):
    if a % 2 == 0:
        alist[i] = 0
    else:
        alist[i] = 1

diffcnt = 0
prev = alist[0]
zeropos = -1
onepos = -1
cnt = 0
for i, a in enumerate(alist):
    if prev != a:
        if diffcnt == 0:
            diffcnt += 1
        else:
            # swap
            if a == 0:
                # 마지막 1의 위치로 옮긴다
                cnt += i - onepos
                alist[onepos], alist[i] = alist[i], alist[onepos]
                onepos = i
            else:
                cnt += i - zeropos
                alist[zeropos], alist[i] = alist[i], alist[zeropos]
                zeropos = i

    if a == 0 and zeropos == -1:
        zeropos = i
    elif a == 1 and onepos == -1:
        onepos = i

    prev = alist[i]

print(cnt)