import sys
input = sys.stdin.readline

n = int(input())
buildings = [int(input()) for _ in range(n)]

stack = []
tot = 0

for building in buildings:
    while stack and stack[-1] <= building :
        stack.pop()
    stack.append(building)

    tot += len(stack) - 1
    
print(tot)