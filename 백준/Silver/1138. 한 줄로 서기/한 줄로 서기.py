import sys
input = sys.stdin.readline

n = int(input())
hints = list(map(int, input().split()))
line = [0] * n

for i, hint in enumerate(hints):
    zerocnt = 0
    idx = hint
    zerocnt = line[:idx].count(0)

    while True:
        if line[idx] == 0:
            if zerocnt == hint:
                line[idx] = i + 1
                break
            else:
                zerocnt += 1
                idx += 1
        else:
            idx += 1

print(*line)