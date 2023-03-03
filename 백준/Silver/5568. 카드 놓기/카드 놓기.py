from itertools import permutations

n = int(input())
k = int(input())
cards = [input() for _ in range(n)]
cases = list(permutations(cards, k))
res = []
for case in cases:
    res.append(''.join(case))
print(len(set(res)))