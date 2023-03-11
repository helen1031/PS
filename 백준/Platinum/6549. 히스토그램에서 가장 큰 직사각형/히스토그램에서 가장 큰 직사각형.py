import sys
input = sys.stdin.readline

while True:
    info = list(map(int, input().split()))
    if info == [0]:
        break
    n = info[0]
    histogram = info[1:]
    
    max_square = 0
    st = []
    for i, histo in enumerate(histogram):
        tmp = i
        while st and st[-1][1] > histo:
            idx, height = st.pop()
            width = i - idx
            max_square = max(max_square, width * height)
            tmp = idx
        st.append((tmp, histo))
        
    while st:
        idx, height = st.pop()
        width = n - idx
        max_square = max(max_square, width * height)
        
    print(max_square)
            
