import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
bstr = str(b)

for i in range(2, -1, -1):
    print(a* int(bstr[i]))
    
print(a*b)