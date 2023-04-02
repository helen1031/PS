import sys
input = sys.stdin.readline

from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for _ in range(int(input())):
    h, w = map(int, input().split())
    graph = [list(map(str, input().rstrip())) for _ in range(h)]
    keys = input().rstrip()
    maxcnt = 0
    unlocked = {}
    for alphabet in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        unlocked[alphabet] = []

    def bfs(sy, sx, cnt):
        global keys

        visited = [[False] * w for _ in range(h)]

        q = deque([(sy, sx)])
        visited[sy][sx] = True

        while q:
            y, x = q.popleft()

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx]:
                    if graph[ny][nx] == ".":
                        q.append((ny, nx))
                        visited[ny][nx] = True
                    elif graph[ny][nx] == "$":
                        cnt += 1
                        graph[ny][nx] = "."
                        q.append((ny, nx))
                        visited[ny][nx] = True
                    elif graph[ny][nx] != "*":
                        if "a" <= graph[ny][nx] <= "z":
                            keys += graph[ny][nx]
                            q.append((ny, nx))
                            visited[ny][nx] = True

                            for ky, kx in unlocked[graph[ny][nx].upper()]:
                                q.append((ky, kx))
                                visited[ky][kx] = True

                            graph[ny][nx] = "."

                        else:
                            door = graph[ny][nx]
                            if door.lower() in keys:
                                graph[ny][nx] = "."
                                q.append((ny, nx))
                                visited[ny][nx] = True
                            else:
                                unlocked[door].append((ny, nx))

        return cnt


    for y in range(h):
        for x in range(w):
            if (y == 0 or x == 0) or (y == h-1 or x == w-1):
                if graph[y][x] == ".":
                    maxcnt += bfs(y, x, 0)
                elif graph[y][x] == "$":
                    graph[y][x] = "."
                    maxcnt += bfs(y, x, 1)
                elif graph[y][x] != "*":
                    if "a" <= graph[y][x] <= "z":
                        keys += graph[y][x]
                        graph[y][x] = "."
                        maxcnt += bfs(y, x, 0)
                    else:
                        door = graph[y][x]
                        if door.lower() in keys:
                            graph[y][x] = "."
                            maxcnt += bfs(y, x, 0)
                        else:
                            unlocked[door].append((y, x))
    print(maxcnt)