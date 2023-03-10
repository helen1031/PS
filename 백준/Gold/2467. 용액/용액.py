import sys
input = sys.stdin.readline

n = int(input())
features = list(map(int, input().split()))
features.sort()

start = 0
end = n -1
ans = abs(features[start] + features[end])
res = [features[start], features[end]]
while start < end:
    mix = features[start] + features[end]
    
    if abs(mix) < ans:
        ans = abs(mix)
        res = [features[start], features[end]]
        if ans == 0:
            break
            
    if mix < 0:
        start += 1
    else:
        end -= 1
        
print(*res)