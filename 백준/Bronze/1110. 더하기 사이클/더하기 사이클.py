n = int(input())
num = str(n)
cnt = 0

while True:
    right = num[-1]
    if len(num) < 2:
        num = str(int(num))
    else:
        num = str(sum(list(map(int, num))))
    if right == "0":
        num = num[-1]
    else:
        num = right + num[-1]
    cnt += 1


    if num == str(n):
        print(cnt)
        break