import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(input().rstrip())

st = []
cnt = 0
for num in nums:
    while st and cnt < k:
        if st[-1] >= num:
            break
        else:
            st.pop()
            cnt += 1
    st.append(num)
            
if cnt < k:
    st = st[:n-k]

print(''.join(st))
    