import sys
input = sys.stdin.readline

n = int(input())
features = list(map(int, input().split())) # 산성 양수, 알칼리성 음수
features.sort()

l = 0
r = n - 1
ans = abs(features[l] + features[r])
res = [features[l], features[r]]
while l < r:
    mix = features[l] + features[r]
    
    if abs(mix) < ans:
        ans = abs(mix)
        res = [features[l], features[r]]
        if ans == 0:
            break
            
    if mix < 0 :
        l += 1
    else:
        r -= 1
    
print(*res)