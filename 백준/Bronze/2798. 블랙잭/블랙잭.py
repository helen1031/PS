import sys
input = sys.stdin.readline

n, m = map(int, input().split())
deck = list(map(int, input().split()))
cards = []
sums = []

def dfs(idx):
    if len(cards) == 3:
        tot = sum(cards)
        if tot <= m:
            sums.append(tot)
        return
    for i in range(idx, n):
        cards.append(deck[i])
        dfs(i+1)
        cards.pop()
dfs(0)

print(max(sums))