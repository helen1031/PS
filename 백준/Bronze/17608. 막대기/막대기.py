import sys
input = sys.stdin.readline

n = int(input())
st = [int(input()) for _ in range(n)]

cnt = 1
curr = st.pop()
while st:
    prev = st.pop()
    if prev > curr:
        cnt += 1
        curr = prev
        
print(cnt)