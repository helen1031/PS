import sys
input = sys.stdin.readline

for _ in range(int(input())):
    case = list(map(int, input().split()))
    n = case[0]
    case = case[1:]
    avg = sum(case) / n
    
    case.sort(reverse=True)
    cnt = 0
    for i in range(len(case)):
        if case[i] > avg:
            cnt += 1
        else:
            break
            
    print("{:.3f}%".format(cnt / n * 100))
    