import sys
input = sys.stdin.readline

h, w = map(int, input().split())
world = list(map(int, input().split()))

cnt = 0

for i in range(1, w-1):
    lmax = max(world[:i])
    rmax = max(world[i+1:])
    height = min(lmax, rmax)

    current = world[i]
    if current < height:
        cnt += height - current

print(cnt)