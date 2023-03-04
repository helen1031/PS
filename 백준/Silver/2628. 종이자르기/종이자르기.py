import sys
input = sys.stdin.readline

w, h = map(int, input().split())
n = int(input())
# 가로 0, 세로 1
row = [0, h]
col = [0, w]
for _ in range(n):
    t, pos = map(int, input().split())
    if t == 0:
        row.append(pos)
    else:
        col.append(pos)
row.sort()
col.sort()

rlen = []
clen = []
for i in range(1, len(row)):
    rlen.append(row[i] - row[i-1])
for i in range(1, len(col)):
    clen.append(col[i] - col[i-1])
    
print(max(rlen)*max(clen))
