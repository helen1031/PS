n, r, c = map(int, input().split()) # 2^n, r행 c열
cnt = 0
def z(nn, nr, nc):
    global cnt
    
    if nn == 1:
        if nr == 0:
            if nc == 0:
                cnt += 0
            else:
                cnt += 1
        else:
            if nc == 0:
                cnt += 2
            else:
                cnt += 3
        return
    
    # 몇 사분면인지 판별한다
    # 쪼개지는 범위에서의 좌표값으로 재설정해준다
    area = 0
    if nr < 2 ** (nn-1):
        if nc < 2 ** (nn-1): area = 1
        else: 
            area = 2
            nc = nc - 2 ** (nn -1)
    else:
        nr = nr -2 ** (nn - 1)
        if nc < 2 ** (nn-1): area = 3
        else: 
            area = 4
            nc = nc - 2 ** (nn -1)
    # =4^n-1 * (사분면 - 1)만큼을 cnt에 더해준다
    cnt += 4 ** (nn-1) * (area - 1)
    # z 함수를 재귀호출한다
    z(nn-1, nr, nc)
    
z(n, r, c)
print(cnt)