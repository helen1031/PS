import sys
input = sys.stdin.readline

n = int(input())
towers = list(map(int, input().split()))
answer = [0] * n
st = []
for i in range(n):
    while st:
        if st[-1][1] > towers[i]:
            answer[i] = st[-1][0] + 1
            break
        else:
            st.pop()
        
    st.append((i, towers[i]))
print(*answer)