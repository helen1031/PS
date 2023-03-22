import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

for _ in range(int(input())):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
        
    visited = [False] * (n + 1)
    team = []
    
    def dfs(start, current):
        global team
        
        cycle.append(current)
        visited[current] = True
        
        nextnode = graph[current]
        
        if visited[nextnode] == False:
            dfs(start, nextnode)
        else:
            if nextnode in cycle:
                team += cycle[cycle.index(nextnode):]
            return
                        
    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            dfs(i, i)
            
    print(n - len(team))