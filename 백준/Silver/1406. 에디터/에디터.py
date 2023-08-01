LeftStack = list(str(input()))
RightStack = []

t = int(input())

for i in range(t):
    command = input().split()
   
    if(command[0] == "L"):
        if(LeftStack): # 스택이 없지 않으면
            RightStack.append(LeftStack.pop())
    elif(command[0] == "D"):
        if(RightStack): # 스택이 없지 않으면
            LeftStack.append(RightStack.pop())
    elif(command[0] == "B"):
        if(LeftStack):
            LeftStack.pop()
    elif(command[0] == "P"):
        LeftStack.append(command[1])

Left = "".join(LeftStack)
Right = "".join(RightStack)

result = Left + Right[::-1]

print(result)