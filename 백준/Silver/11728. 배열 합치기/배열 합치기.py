import sys

n, m = map(int, input().strip().split())
alist = list(map(int, input().strip().split()))
blist = list(map(int, input().strip().split()))

clist = alist + blist
clist.sort()

print(*clist)
