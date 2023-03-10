import sys
input = sys.stdin.readline

import heapq

left = [] # maxheap - 음수 곱해야함
right = [] # minheap

for _ in range(int(input())):
    num = int(input())
    # left에 삽입해야 하는 경우
    if len(left) == len(right):
        if len(left) == 0:
            heapq.heappush(left, -num)
        else:
            if num <= right[0]:
                heapq.heappush(left, -num)
            # 오른쪽 min 값보다 num이 큰 경우 - 오른쪽에 있는 min값을 왼쪽으로 옮겨줘야 한다
            else:
                tmp = heapq.heappop(right)
                heapq.heappush(left, -tmp)
                heapq.heappush(right, num)
    # right에 삽입해야 하는 경우
    else:
        if -num <= left[0]:
            heapq.heappush(right, num)
        else:
            tmp = heapq.heappop(left)
            heapq.heappush(right, -tmp)
            heapq.heappush(left, -num)
    print(-left[0])