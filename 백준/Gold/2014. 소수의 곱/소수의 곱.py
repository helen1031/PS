import sys
input = sys.stdin.readline

import heapq

k, n = map(int, input().split())
primes = list(map(int, input().split()))

hq = []
for prime in primes:
    heapq.heappush(hq, prime)

for _ in range(n): # 최소 숫자
    num = heapq.heappop(hq)
    for i in range(k): # 2 3 5 7
        tmp = num * primes[i]
        heapq.heappush(hq, tmp)
        # 중복 제거?
        if num % primes[i] == 0:
            break

print(num)