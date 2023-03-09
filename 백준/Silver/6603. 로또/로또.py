from itertools import combinations

while True:
    tmp = list(map(int, input().split()))
    if tmp == [0]:
        break
    else:
        k = tmp[0]
        s = tmp[1:]

        cases = combinations(s, 6)
        for case in cases:
            print(*case)
    print()