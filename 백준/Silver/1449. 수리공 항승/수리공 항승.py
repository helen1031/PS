import sys
input = sys.stdin.readline

n, l = map(int, input().split())
positions = list(map(int, input().split()))
positions.sort()

cnt = 1
current = positions[0]
current_start = current - 0.5
current_end = current_start + l
for i, position in enumerate(positions[1:]):
    if current_start <= position <= current_end:
        continue
    else:
        if position > current_end:
            cnt += 1
            current_start = position - 0.5
            current_end = current_start + l
print(cnt)