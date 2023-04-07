import sys
input = sys.stdin.readline

n, l = map(int, input().split())
candidates = [input().rstrip() for _ in range(n)]
candidates.sort()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

possible = set()

def dfs(current, string, idx, diffcnt):
    if len(string) == l:
        possible.add(string)
        return

    for alpha in alphabet:
        if alpha != current[idx]:
            if diffcnt == 1:
                continue
            else:
                dfs(current, string+alpha, idx + 1, diffcnt + 1)
        else:
            dfs(current, string+alpha, idx+1, diffcnt)

for candidate in candidates:
    dfs(candidate, "", 0, 0)

newpossible = []
for current in possible:
    allpass = True
    for compare in candidates:
        diffcnt = 0
        for i in range(l):
            if current[i] != compare[i]:
                diffcnt += 1
                if diffcnt == 2:
                    allpass = False
                    break
        if not allpass:
            break

    if allpass:
        newpossible.append(current)

if newpossible:
    print(newpossible[0])
else:
    print("CALL FRIEND")