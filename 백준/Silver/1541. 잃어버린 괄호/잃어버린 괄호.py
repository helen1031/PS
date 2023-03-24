import sys
input = sys.stdin.readline

# 입력 전처리 - 숫자와 기호 분리
s = input().rstrip()
operands = []
for c in s:
    if c in ('-', '+'):
        operands.append(c)
s = s.replace("+", " ")
s = s.replace("-", " ")
nums = list(map(int, s.split()))

a = nums[0]
b = 0
nums = nums[1:]

for i, operand in enumerate(operands):
    if operand == '+':
        if b == 0:
            a += nums[i]
        else:
            b += nums[i]
    else:
        if b == 0:
            b += nums[i]
        else:
            a = a - b
            b = nums[i]
            
print(a-b)