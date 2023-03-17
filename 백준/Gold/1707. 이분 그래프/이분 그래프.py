import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (v + 1)
    cycle = False
    
    def dfs(x, prv):
        global cycle
        
        if cycle :
            return
        
        visited[x] = prv
        for i in graph[x]:
            if not visited[i]:
                dfs(i, -prv)    #그래프의 정점을 두가지 색으로 칠할 때, 인접한 정점끼리는 다른 색을 가지고 있는 그래프
            elif visited[x] == visited[i]:
                cycle = True
                return
    
    for i in range(1, v + 1):
        if not visited[i]:
            dfs(i, 1)
            if cycle:
                break
                
    if cycle:
        print("NO")
    else:
        print("YES")