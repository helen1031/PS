import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(input().rstrip())
st = []
cnt = 0
for num in nums:
    while st and cnt < k:
        if st[-1] < num:
            st.pop()
            cnt += 1
        else:
            break
    st.append(num)
    
if len(st) > n - k:
    st = st[:n-k]
    
print(''.join(st))