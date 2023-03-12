import sys
input = sys.stdin.readline

string = input().rstrip()
bomb = input().rstrip()

st = []
for s in string:
    st.append(s)
    if s == bomb[-1] and st[-len(bomb):] == list(bomb):
        for i in range(len(bomb)):
            st.pop()

if not st:
    print("FRULA")
else: 
    print(''.join(st))