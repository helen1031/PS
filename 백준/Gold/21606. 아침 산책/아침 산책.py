import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
inside = [0]
for i in list(map(int, input().rstrip())):
    inside.append(i)
graph = [[] for _ in range(n + 1)]

while True:
    try:
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    except:
        break
        
cnt = 0
visited = [False] * (n + 1)

def dfs(current, visited):
    global cnt
    
    if inside[current]:
        cnt += 1
        return
    
    for nextpath in graph[current]:
        if not visited[nextpath]:
            visited[nextpath] = True
            dfs(nextpath, visited)
            visited[nextpath] = False


for start in range(1, n + 1):
    if inside[start]:
        visited[start] = True
        dfs(start, visited)
        visited[start] = False
        
print(cnt)