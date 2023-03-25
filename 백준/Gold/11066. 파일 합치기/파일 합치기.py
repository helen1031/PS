import sys
input = sys.stdin.readline
MAX = sys.maxsize

for _ in range(int(input())):
    k = int(input())
    files = list(map(int, input().split()))
    
    dp = [[0] * k for _ in range(k)]
    
    sums = [0] # 누적합
    for file in files:
        sums.append(sums[-1] + file)
        
    for d in range(1, k): # 대각선
        for i in range(0, k -d): # 행
            j = i + d # 열
            dp[i][j] = MAX
            for x in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][x] + dp[x+1][j] + sums[j+1] - sums[i])
                
    print(dp[0][-1])