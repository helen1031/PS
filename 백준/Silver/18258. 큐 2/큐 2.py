import sys
input = sys.stdin.readline

from collections import deque

q = deque()
for _ in range(int(input())):
    op = list(map(str, input().split()))
    if op[0] == "push":
        q.append(op[1])
    elif op[0] == "pop":
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif op[0] == "size":
        print(len(q))
    elif op[0] == "empty":
        if q:
            print("0")
        else:
            print("1")
    elif op[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)
        