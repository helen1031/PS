import sys
input = sys.stdin.readline

score = int(input())
cal = score // 10
if cal >= 9 :
    print("A")
elif cal >= 8:
    print("B")
elif cal >= 7:
    print("C")
elif cal >= 6:
    print("D")
else:
    print("F")