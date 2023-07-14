import sys
input = sys.stdin.readline

n = int(input())
word = input().rstrip()

straight = False
result = 0
temp = 0
for char in word:
    if char in "0123456789":
        straight = True
        temp = temp * 10 + int(char)
    else:
        if straight:
            result += temp
            temp = 0
            straight = False
            
if temp != 0:
    result += temp
print(result)