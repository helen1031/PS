import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
inside = [0] + list(map(int, input().rstrip()))
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

# case 1: 실내 ~ 실내
case1 = 0
while True:
    try:
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        if inside[a] and inside[b]:
            case1 += 2
    except:
        break

def dfs(current, cnt):
    
    visited[current] = True
    
    for nextpath in graph[current]:
        # 실내를 만나면 cnt + 1
        if inside[nextpath]:
            cnt += 1
        # 실외 덩어리는 dfs
        elif not visited[nextpath] and not inside[nextpath]:
            cnt = dfs(nextpath, cnt)
    return cnt

# case 2 : 실내 ~ 실외덩어리 ~ 실내
case2 = 0
for start in range(1, n + 1):
    if not visited[start] and not inside[start]:
        x = dfs(start, 0)
        case2 += x * (x - 1)
        
print(case1 + case2)
