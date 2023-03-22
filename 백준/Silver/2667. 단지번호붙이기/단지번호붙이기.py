n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(y, x, tmp):
    if (x <= -1 or x>= n) or (y <= -1 or y >= n):
        return False

    if graph[y][x] == 1:
        graph[y][x] = 0
        global cnt          ##
        cnt += 1            ##

        DFS(y + dy[0], x + dx[0], tmp)
        DFS(y + dy[1], x + dx[1], tmp)
        DFS(y + dy[2], x + dx[2], tmp)
        DFS(y + dy[3], x + dx[3], tmp)

        return True

    return False

cnt = 0     
cnts = []
for y in range(n):
    for x in range(n):
        if DFS(y, x, 0):
            cnts.append(cnt)    ##
            cnt = 0             ##

print(len(cnts))
cnts.sort()
for i in range(len(cnts)):
    print(cnts[i])