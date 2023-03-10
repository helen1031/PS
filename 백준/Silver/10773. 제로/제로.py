import sys
input = sys.stdin.readline

st = []
for _ in range(int(input())):
    n = int(input())
    if n != 0:
        st.append(n)
    else:
        st.pop()
        
print(sum(st))