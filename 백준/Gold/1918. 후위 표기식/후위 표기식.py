import sys
input = sys.stdin.readline

statement = list(input().rstrip())
st = []
res = ""

for s in statement:
    if s not in "+-*/()":
        res += s
    else:
        if s == "(":
            st.append(s)
        elif s == ")":
            while st and st[-1] != "(":
                res += st.pop()
            st.pop()
        elif s in "*/":
            while st and st[-1] in "*/":
                res += st.pop()
            st.append(s)
        else:
            while st and st[-1] != "(":
                res += st.pop()
            st.append(s)
            
while st:
    res += st.pop()
    
print(res)
    
    