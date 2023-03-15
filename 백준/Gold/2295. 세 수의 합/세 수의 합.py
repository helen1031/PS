import sys
input = sys.stdin.readline

n = int(input())
u = set([int(input()) for _ in range(n)])

absum = set()

# x + y = k - z
for x in u:
    for y in u:
        absum.add(x + y)

ans = []
for k in u:
    for z in u:
        if k - z in absum:
            ans.append(k)
                
print(max(ans))
    