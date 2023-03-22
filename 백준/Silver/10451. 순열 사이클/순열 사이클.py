import sys
input = sys.stdin.readline

def dfs(start, current):
    global cycle
    nextnum = graph[current]
    if visited[nextnum]:
        if nextnum == start:
            cycle += 1
            return
    else:
        visited[nextnum] = True
        dfs(start, nextnum)
        

for _ in range(int(input())):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    cycle = 0
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            dfs(i, i)
            
    print(cycle)
