import sys
input = sys.stdin.readline

n = int(input())
circles = []
for _ in range(n):
    x, r = map(int, input().split())
    circles.append([x-r, -r, '('])
    circles.append([x+r, r, ')'])
circles.sort(key = lambda x:(x[0], -ord(x[2]), x[1]))

st = []
area = 1
for i, circle in enumerate(circles):
    if circle[2] == '(':
        st.append(circle)
    else:
        length = 0
        while st:
            pos, r, shape = st.pop()
            if shape == '(':
                if abs(r) == length:
                    area += 2
                else:
                    area += 1
                st.append([pos, abs(r), 'O'])
                break
            else:
                length += r
print(area)