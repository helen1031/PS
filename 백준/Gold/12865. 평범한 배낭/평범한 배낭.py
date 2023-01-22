import sys
n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]
knapsack = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for w in range(1, k+1):
        weight = items[i-1][0]
        value = items[i-1][1]
        
        if w < weight:
            knapsack[i][w] = knapsack[i-1][w]
        else:
            knapsack[i][w] = max(value + knapsack[i-1][w-weight], knapsack[i-1][w])
            
print(knapsack[n][k])