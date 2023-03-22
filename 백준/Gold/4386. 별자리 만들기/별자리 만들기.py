import sys
input = sys.stdin.readline

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
    
n = int(input())
stars = []
for _ in range(n):
    x, y = map(float, input().split())
    stars.append((x, y))
parent = [i for i in range(n + 1)]

edges = []
for i in range(n-1):
    for j in range(i + 1, n):
        ax, ay = stars[i]
        bx, by = stars[j]
        cost = ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5
        edges.append((cost, (i+1, ax, ay), (j+1, bx, by)))
    
edges.sort()

ans = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a[0]) != find_parent(parent, b[0]):
        union_parent(parent, a[0], b[0])
        ans += cost
        
print(round(ans, 2))
    