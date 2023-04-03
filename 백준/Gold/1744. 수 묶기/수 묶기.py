import sys
input = sys.stdin.readline

n = int(input())
negative = []
positive = []
lsum = 0
for _ in range(n):
    num = int(input())
    if num > 1:
        positive.append(num)
    elif num == 1:
        lsum += 1
    else:
        negative.append(num)

positive.sort()
negative.sort(reverse=True)


# 양수
if positive:
    if len(positive) % 2 == 0:
        while positive:
            a = positive.pop()
            b = positive.pop()
            lsum += a * b
    else:
        if len(positive) != 1:
            while len(positive) > 1:
                a = positive.pop()
                b = positive.pop()
                lsum += a * b
        lsum += positive[0]

# 음수
if negative:
    if len(negative) % 2 == 0:
        while negative:
            a = negative.pop()
            b = negative.pop()
            lsum += a * b
    else:
        if len(negative) != 1:
            while len(negative) > 1:
                a = negative.pop()
                b = negative.pop()
                lsum += a * b
        lsum += negative[0]

print(lsum)