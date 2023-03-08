import sys

N = int(sys.stdin.readline().rstrip())
power = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
used = [False for _ in range(N)]
answer = 10000

# level은 선택한 갯수
def dfs(count:int, idx:int):
    if count == N//2:
        LINK = 0
        START = 0
        for i in range(N):
            if used[i]:
                for j in range(i + 1, N):
                    if used[j]:
                        START += power[i][j]
                        START += power[j][i]
            else:
                for j in range(i + 1, N):
                    if used[j] is False:
                        LINK += power[i][j]
                        LINK += power[j][i]
        global answer
        if abs(START - LINK) < answer:
            answer = abs(START - LINK)
            if answer == 0:
                print(0)
                exit()

    for now in range(idx, N):
        if used[now]:
            continue
        used[now] = True
        dfs(count + 1, now + 1)
        used[now] = False

dfs(0, 0)
print(answer)