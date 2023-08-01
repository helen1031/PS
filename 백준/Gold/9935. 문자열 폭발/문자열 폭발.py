import sys
input = sys.stdin.readline

string = input().strip()
bomb = input().strip()
st = []
for s in string:
    st.append(s)
    if s == bomb[-1] and "".join(st[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            st.pop()
            
if not st:
    print("FRULA")
else:
    print("".join(st))