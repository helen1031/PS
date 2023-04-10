import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    costs = list(map(int, input().split()))

    profit = 0
    maxcost = costs[-1]
    
    for day in range(n-2, -1, -1):
        cost = costs[day]
        if cost <= maxcost:
            profit += maxcost - cost
        else:
            maxcost = cost
    print(profit)