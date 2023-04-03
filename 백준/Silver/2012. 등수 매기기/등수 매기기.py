import sys
input = sys.stdin.readline

n = int(input())
predicts = [int(input()) for _ in range(n)]
predicts.sort()

dislike = 0
rank = 1
for i, predict in enumerate(predicts):
    dislike += abs(predict - rank)
    rank += 1

print(dislike)