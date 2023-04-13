import sys
input = sys.stdin.readline

stack = []

string = input().rstrip()
dic = {"H": 1, "C": 12, "O": 16}

for char in string:
    if char in "23456789":
        tmp = stack.pop()
        stack.append(tmp * int(char))

    elif char in "(":
        stack.append(char)

    elif char in "HCO":
        stack.append(dic[char])

    else:
        tmp = 0
        while stack[-1] != "(":
            tmp += stack.pop()
        stack.pop() #  ( 괄호 pop
        stack.append(tmp)

answer = 0
while stack:
    answer += stack.pop()
print(answer)