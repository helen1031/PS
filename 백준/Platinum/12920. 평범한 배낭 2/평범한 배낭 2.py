import sys
input = sys.stdin.readline

n, m = map(int, input().split())
items = [(0,0)] #무게, 만족도
for _ in range(n):
    v, c, k = map(int, input().split()) # 무게, 만족도, 개수
    # 2의 제곱수 만큼 - 종류별로 하나씩 다 더해주면 메모리 초과 발생
    i = 1
    while k > 0:
        tmp = min(i, k)
        items.append((v * tmp, c * tmp))
        k -= i
        i *= 2

n = len(items) - 1
knapsack = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
for i in range(1, n+1):
    for w in range(1, m+1):
        weight = items[i][0]
        value = items[i][1]
        
        if weight > w :
            knapsack[i][w] = knapsack[i-1][w]
        else:
            knapsack[i][w] = max(value + knapsack[i-1][w-weight], knapsack[i-1][w])
            
print(knapsack[n][m])