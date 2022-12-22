n = int(input())
a = [0 for _ in range(n)]
b = list(map(int, input().split()))

cnt = 0
while a != b:
    for i in range(n):
        if b[i] % 2 == 1:
            b[i] -= 1
            cnt += 1
            
    if a == b:
        break
    
    for i in range(n):
        b[i] = b[i] // 2
    cnt += 1
    
print(cnt)