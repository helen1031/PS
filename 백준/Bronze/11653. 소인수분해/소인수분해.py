n = int(input())

nums = []
while n != 1:
    for i in range(2, n+1):
        if n % i == 0:
            n = n // i
            nums.append(i)
            break
            
for num in nums:
    print(num)