from collections import deque

def BFS(current, time, dst, visited):
    queue = deque([(current, time)])

    while queue:
        x = queue.popleft()
        #print(x)
        xx = x[0]
        xt = x[1]

        if not visited[xx]:
            visited[xx] = True

            if(xx == dst):
                return xt

            else:
                if(xx+1) <= 100000:
                    queue.append((xx+1, xt+1))
                if(xx-1) >= 0:
                    queue.append((xx-1, xt+1))
                if(xx*2) <= 100000:
                    queue.append((2*x[0], xt+1))
    return xt

N, K = map(int, input().split())
visited = [False] * 1000001
print(BFS(N, 0, K, visited))