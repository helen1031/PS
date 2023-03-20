import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
tmp = list(map(int, input().split()))
pplnum = tmp[0]
ppllist = tmp[1:]
for ppl in ppllist:
    parent[ppl] = 0

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parties = []
for _ in range(m):
    p_tmp = list(map(int, input().split()))
    p_pplnum = p_tmp[0]
    p_ppllist = p_tmp[1:]
    for i in range(p_pplnum-1):
        union_parent(parent, p_ppllist[i], p_ppllist[i+1])
    parties.append(p_ppllist)
    
cnt = 0
for party in parties:
    truth = False
    for i in range(len(party)):
        if find_parent(parent, party[i]) == 0:
            truth = True
            break
    if not truth:
        cnt += 1
        
print(cnt)