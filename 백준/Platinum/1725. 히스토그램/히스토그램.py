import sys
input = sys.stdin.readline

n = int(input())
histogram = [int(input()) for _ in range(n)]

max_square = 0
stack = []
for i, histo in enumerate(histogram):
    tmp = i
    while stack and stack[-1][1] > histo:
        idx, height = stack.pop()
        width = i - idx
        max_square = max(max_square, width * height)
        tmp = idx
    stack.append([tmp, histo])
    
while stack:
    idx, height = stack.pop()
    width = n - idx
    max_square = max(max_square, width * height)
    
print(max_square)