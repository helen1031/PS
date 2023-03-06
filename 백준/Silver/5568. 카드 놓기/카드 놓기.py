import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
deck = [int(input()) for _ in range(n)]
used = [False] * n
cards = []
res = []

def dfs():
    if len(cards) == k:
        res.append(''.join(cards))
        return
    
    # 순열 구하기
    for i in range(n):
        if not used[i]:
            cards.append(str(deck[i]))
            used[i] = True
            dfs()
            cards.pop()
            used[i] = False
    
dfs()
print(len(set(res)))