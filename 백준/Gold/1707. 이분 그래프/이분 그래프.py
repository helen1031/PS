import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    visited = [False] * (v+1)
    cycle = False
    
    def dfs(cur, group):
        global cycle
        
        if cycle:
            return
        
        visited[cur] = group
        
        for x in graph[cur]:
            if not visited[x]:
                dfs(x, -group)
            elif visited[cur] == visited[x]:
                cycle = True
                return
                
        
    for i in range(1, v+1):
        if not visited[i]:
            dfs(i, 1)
            if cycle:
                break
    
    if cycle:
        print("NO")
    else:
        print("YES")