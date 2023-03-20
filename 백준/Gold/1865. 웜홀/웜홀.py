import sys
input = sys.stdin.readline

INF = int(1e9)

for _ in range(int(input())):
    n, m, w = map(int, input().split())
    
    def bf():
        for i in range(n):
            for j in range(len(edges)):
                cur_node = edges[j][0]
                next_node = edges[j][1]
                cost = edges[j][2]
            
                if dist[next_node] > dist[cur_node] + cost:
                    dist[next_node] = dist[cur_node] + cost
                    if i == n - 1:
                        return True
        return False
    
    edges = []
    dist = [INF] * (n + 1)
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
        
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))
    
    neg_cycle = bf()
      
    if neg_cycle:
        print("YES")
    else:
        print("NO")