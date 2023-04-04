import sys
input = sys.stdin.readline

n = int(input())
predicts = [int(input()) for _ in range(n)]
predicts.sort()

dislikes = 0

rank = 1
for predict in predicts:
    dislikes += abs(predict - rank)
    rank += 1

print(dislikes)