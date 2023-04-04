import sys
input = sys.stdin.readline

n = int(input())

def isSosu(num):
    if num == 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

stack = []
def recursion():
    if len(stack) == n:
        print(*stack, sep="")
        return

    for i in range(1, 10):
        stack.append(str(i))
        if isSosu(int(''.join(stack))):
            recursion()
        stack.pop()

recursion()