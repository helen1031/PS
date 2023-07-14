import sys
input = sys.stdin.readline

a, b = map(int, input().split())
alist = set(map(int, input().split()))
blist = set(map(int, input().split()))

aside = len(alist-blist)
bside = len(blist-alist)

print(aside+bside)