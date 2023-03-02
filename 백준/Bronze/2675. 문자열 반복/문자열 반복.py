import sys
input = sys.stdin.readline

for _ in range(int(input())):
    r, s = map(str, input().rstrip().split())
    
    res = ""
    for c in s:
        res += c * int(r)
        
    print(res)