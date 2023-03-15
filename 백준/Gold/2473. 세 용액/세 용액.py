import sys
input = sys.stdin.readline

n = int(input())
features = list(map(int, input().split()))
features.sort()

minabs = 3000000000
ans = []
for i, feature in enumerate(features):
    left = i + 1
    right = n - 1
    while left < right:
        mix = feature + features[left] + features[right]
        if abs(mix) <= minabs:
            ans = [feature, features[left], features[right]]
            minabs = abs(mix)
        if mix < 0 :
            left += 1
        elif mix == 0:
            print(*ans)
            exit()
        else:
            right -= 1
            
print(*ans)
        