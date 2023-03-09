import sys
input = sys.stdin.readline

from itertools import permutations

n, m = map(int, input().split())
ns = [i+1 for i in range(n)]
cases = list(permutations(ns, m))
cases.sort()
for case in cases:
    print(*case)
