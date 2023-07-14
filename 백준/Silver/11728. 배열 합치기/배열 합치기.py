import sys
input = sys.stdin.readline

n, m = map(int, input().split())
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))

clist = alist + blist;
clist.sort()

print(*clist)
