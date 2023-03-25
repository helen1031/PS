import sys
input = sys.stdin.readline

n = int(input())
tmpdp = list(map(int, input().split()))
maxdp = mindp = tmpdp

for _ in range(n-1):
    a, b, c = map(int, input().split())
    maxdp = [a + max(maxdp[:-1]), b + max(maxdp), c + max(maxdp[1:])]
    mindp = [a + min(mindp[:-1]), b + min(mindp), c + min(mindp[1:])]
    
print(max(maxdp), min(mindp))