import sys
input = sys.stdin.readline

def calculate_dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def solve(points, n):
    if n == 2:
        return calculate_dist(points[0], points[1])
    if n == 3:
        return min(calculate_dist(points[0], points[1]),
                   calculate_dist(points[1], points[2]),
                   calculate_dist(points[2], points[0]))

    mid_line = (points[n//2 - 1][0] + points[n//2][0]) // 2
    distance = min(solve(points[:n//2], n//2), solve(points[n//2:], n//2))
    candidates = []
    for point in points:
        if (mid_line - point[0]) ** 2 <= distance:
            candidates.append(point)

    candidates.sort(key = lambda x:x[1])
    if len(candidates) == 1:
        return distance
    else:
        ycheck = distance
        for i in range(len(candidates) -1):
            for j in range(i + 1, len(candidates)):
                if (candidates[i][1] - candidates[j][1]) ** 2 > distance:
                    break
                ycheck = min(ycheck, calculate_dist(candidates[i], candidates[j]))

    return ycheck

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

pointsset = list(set(map(tuple, points)))
if len(points) != len(pointsset):
    print(0)
else:
    points.sort()
    print(solve(points, n))