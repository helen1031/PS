import sys
input = sys.stdin.readline

from collections import deque

s = list(input().rstrip())
s.reverse()

apos = deque()
bpos = deque()
cpos = deque()
for idx, char in enumerate(s):
    if char == 'A':
        apos.append(idx)
    elif char == 'B':
        bpos.append(idx)
    else:
        cpos.append(idx)

cnt = 0
for a in apos:
    while bpos and a > bpos[0]:
        bpos.popleft()
        cnt += 1
        break

for b in bpos:
    while cpos and b > cpos[0]:
        cpos.popleft()
        cnt += 1
        break

print(cnt)