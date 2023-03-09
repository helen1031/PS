import sys
input = sys.stdin.readline

n = int(input())
turn = [list(map(int, input().split())) for _ in range(n)]
# 숫자 하나가 동일한 자리면 strike
# 숫자 포함이면 ball

def check(x, y, z):
    for t in turn:
        question, strike, ball = str(t[0]), t[1], t[2]
        # strike
        scnt = 0
        if question[0] == x:
            scnt += 1
        if question[1] == y:
            scnt += 1
        if question[2] == z:
            scnt += 1

        if scnt != strike:
            return False

        # ball
        bcnt = 0
        if x in question and question[0] != x:
            bcnt += 1
        if y in question and question[1] != y:
            bcnt += 1
        if z in question and question[2] != z:
            bcnt += 1

        if bcnt != ball:
            return False

    return True


# 9 * 9 * 9 전체 숫자 돈다
# 해당 숫자가 모든 질문을 충족하는지 확인한다
# 질문 충족하면 + 1
ans = 0
for x in range(1, 10):
    for y in range(1, 10):
        if y == x:
            continue
        for z in range(1, 10):
            if x == z or y == z:
                continue
            if check(str(x), str(y), str(z)):
                ans += 1

print(ans)
