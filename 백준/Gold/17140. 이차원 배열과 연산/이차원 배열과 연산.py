import sys
input = sys.stdin.readline

from collections import Counter

r, c, k = map(int, input().split())
r, c = r-1, c-1

a = [list(map(int, input().split())) for _ in range(3)]

time = 0

def cal(a, dir):
    new_a = []
    maxlen = 0

    if dir == "C":
        a = list(zip(*a))

    for row in a:
        counter = Counter(row)

        tmp = []
        for cntr in counter.items():
            if cntr[0] == 0:
                continue
            tmp.append((cntr[0], cntr[1]))
        tmp.sort(key=lambda x: (x[1], x[0]))

        new_row = []
        for t in tmp:
            new_row.append(t[0])
            new_row.append(t[1])
        new_a.append(new_row)
        maxlen = max(maxlen, len(new_row))

    for row in new_a:
        while len(row) < maxlen:
            row.append(0)
        if len(row) > 100:
            row = row[:100]
    return new_a if dir == "R" else list(zip(*new_a))

while True:
    if time > 100:
        time = -1
        break

    if r < len(a) and c < len(a[0]) and a[r][c] == k:
        break

    if len(a) >= len(a[0]):
        a = cal(a, "R")
    else:
        a = cal(a, "C")
    time += 1

print(time)