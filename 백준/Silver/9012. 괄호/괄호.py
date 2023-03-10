import sys
input = sys.stdin.readline

for _ in range(int(input())):
    st = []
    data = list(input().rstrip())
    
    sig = 1
    for d in data:
        if d == "(":
            st.append("(")
        else:
            if st:
                st.pop()
            else:
                sig = 0
                break
    
    if sig == 1 and len(st) == 0:
        print("YES")
    else:
        print("NO")