import sys
input = sys.stdin.readline

for _ in range(int(input())):
    res = input().rstrip()
    tot = 0
    tmp = 0
    for i in range(len(res)):
        if res[i] == "O":
            tmp += 1
            tot += tmp
        else:
            tmp = 0
    print(tot)