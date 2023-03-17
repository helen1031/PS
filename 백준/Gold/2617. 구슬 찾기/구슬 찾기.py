import sys
input = sys.stdin.readline

n, m = map(int, input().split())
upper = [[] for _ in range(n + 1)] # 가볍 -> 무겁
lower = [[] for _ in range(n + 1)] # 무겁 -> 가볍

for _ in range(m):
    heavy, light = map(int, input().split())
    upper[light].append(heavy)
    lower[heavy].append(light)
    
visited = [False] * (n + 1)
check = 0

def dfs(graph, x):
    global check
    
    visited[x] = True
    
    for i in graph[x]:
        if not visited[i]:
            check += 1
            dfs(graph, i)
            
cnt = 0
mid = (n + 1) // 2
for i in range(1, n+1):
    visited = [False] * (n + 1)
    check = 0
    
    # upper 탐색
    dfs(upper, i)
    if check >= mid:
        cnt += 1
    
    check = 0
    visited = [False] * (n + 1)
    
    # lower 탐색
    dfs(lower, i)
    if check >= mid:
        cnt += 1
        
print(cnt)