import sys
input = sys.stdin.readline

import heapq, math

for _ in range(int(input())):
    m = int(input())
    cnt = math.ceil(m/10)
    nums = []
    for _ in range(cnt):
        tmp = list(map(int, input().split()))
        for t in tmp:
            nums.append(t)

    left = []  # maxheap
    right = []  # minheap
    alen = 0
    ans = []
    for i, num in enumerate(nums):
        if i % 2 == 0:
            alen += 1
            heapq.heappush(left, -num)
        else:
            heapq.heappush(right, num)

        if right and -left[0] > right[0]:
            l = heapq.heappop(left)
            r = heapq.heappop(right)
            heapq.heappush(left, -r)
            heapq.heappush(right, -l)

        if i % 2 == 0:
            ans.append(-left[0])

    print(alen)
    for i in range(0, alen, 10):
        print(*ans[i:i + 10])
