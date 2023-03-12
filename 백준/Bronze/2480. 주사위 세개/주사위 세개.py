dices = list(map(int, input().split()))
nums = [0 for _ in range(7)]

for dice in dices:
    nums[dice] += 1
    
if 3 in nums:
    print(10000 + nums.index(3) * 1000)
elif 2 in nums:
    print(1000 + nums.index(2) * 100)
else:
    cnt = 0
    for i in range(7):
        if nums[i] == 1:
            cnt += 1
            if cnt == 3:
                break
    print(i * 100)