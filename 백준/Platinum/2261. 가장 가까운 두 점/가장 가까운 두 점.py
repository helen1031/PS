def dist(x1, x2):
    return (x1[0] - x2[0]) ** 2 + (x1[1] - x2[1]) ** 2


# 이론 블로그 참고
def solve(coords, N):
    # 점이 두 개일때는 두점 거리만 구하면 됩니다.
    if N == 2:
        return dist(coords[0], coords[1])
    # 점이 세 개일때는 각 두점 사이의 거리를 구해서 최솟값을 구하면 됩니다.
    elif N == 3:
        return min(dist(coords[0], coords[1]), dist(coords[1], coords[2]), dist(coords[0], coords[2]))
    # ?
    line = (coords[N // 2][0] + coords[N // 2 - 1][0]) // 2
    #print()
    #print("idx: ", N // 2)
    #print("코드스:", coords[N // 2][0], coords[N // 2 - 1][0])
    #print("line:", line)
    # x축을 기준으로 짧은 거리 d를 구합니다.
    d = min(solve(coords[:N // 2], N // 2), solve(coords[N // 2:], N // 2))
    #print("d: ", d)
    # x 축 기준을 잊지 말것
    # 유효 거리 d보다 짧거나 같은 것을 제외하고 나머지는 제외시킵니다.
    # 즉, 두점 거리가 d보다 먼 경우는 제외합니다.
    shortCheck = []
    for subset in coords:
        if (line - subset[0]) ** 2 <= d:
            shortCheck.append(subset)

    shortCheck.sort(key=lambda x: x[1])  # y 좌표 정렬
    # print("shortcheck:", shortCheck)

    if (len(shortCheck) == 1):
        return d
    else:
        yCheck = d
        # x축만 고려하면 아직 고려해야할 점의 개수가 많이 남아있어 시간초과가 뜨게 됩니다.
        # 따라서 y축을 고려해주어 y축 기준의 d보다 긴 경우는 전부 제외시켜 주어야 합니다.
        # 세 가지 경우는 필수로 제외합니다.
        for i in range(len(shortCheck) - 1):
            for j in range(i + 1, len(shortCheck)):
                # y축 기준, 기본적으로 최소 길이 d보다 사이 거리가 긴 경우 제외
                if (shortCheck[i][1] - shortCheck[j][1]) ** 2 > d:
                    break

                yCheck = min(yCheck, dist(shortCheck[i], shortCheck[j]))
    return yCheck


N = int(input())
coords = [list(map(int, input().split())) for _ in range(N)]

coordsSet = list(set(map(tuple, coords)))  # set 정렬(집합)

if len(coordsSet) != len(coords):
    print("0")
else:
    coordsSet.sort()
    # print("coordeset:", coordsSet)
    print(solve(coordsSet, N))