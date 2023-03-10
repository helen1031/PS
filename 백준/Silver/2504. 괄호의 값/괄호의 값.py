st = []
string = list(input().rstrip())
res = 0
tmp = 1
for i in range(len(string)):
    if string[i] == "(":
        st.append("(")
        tmp *= 2
    elif string[i] == "[":
        st.append("[")
        tmp *= 3
    elif string[i] == ")":
        if not st or st[-1] != "(":
            res = 0
            break
        if string[i-1] == "(":
            res += tmp
        tmp //= 2
        st.pop()
    else:
        if not st or st[-1] != "[":
            res = 0
            break
        if string[i-1] == "[":
            res += tmp
        tmp //= 3
        st.pop()

if st:
    print(0)
else:
    print(res)
    
        