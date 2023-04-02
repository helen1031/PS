n = int(input())
schedule = []
for i in range(n):
    schedule.append(list(map(int, input().split())))

dp = [0] * (n+1)
maxp = 0
#일자역순
for i in range(n-1, -1, -1):
    t = i + schedule[i][0] # 상담 마치는 시점
    # 상담 종료일이 기간 내
    if t <= n:
        dp[i] = max(schedule[i][1] + dp[t], maxp)   #오늘 상담 가격 + 상담종료일 이후 얻는 금액
        maxp = dp[i]
    # 기간 외
    else:
        dp[i] = maxp
print(maxp)