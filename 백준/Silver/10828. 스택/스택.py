import sys
input = sys.stdin.readline
st = []

for _ in range(int(input())):
    op = list(map(str, input().rstrip().split()))
    if op[0] == "push":
        st.append(int(op[1]))
    elif op[0] == "pop":
        if len(st) != 0:
            print(st.pop())
        else:
            print(-1)
    elif op[0] == "size":
        print(len(st))
    elif op[0] == "empty":
        if len(st) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(st) == 0:
            print(-1)
        else:
            print(st[-1])