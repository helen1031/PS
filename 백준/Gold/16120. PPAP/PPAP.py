import sys
input = sys.stdin.readline

string = input().rstrip()
CHECK = "PPAP"

if len(string) == len(CHECK):
    if string == "PPAP":
        print("PPAP")
    else:
        print("NP")
    exit()


stack = []
for s in string:
    stack.append(s)
    if s == "P" and ''.join(stack[-4:]) == CHECK:
        for _ in range(4):
            stack.pop()
        stack.append(s)

if ''.join(stack) in ("P", "PPAP"):
    print("PPAP")
else:
    print("NP")
