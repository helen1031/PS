import sys
input = sys.stdin.readline

n = int(input())
words = list(set([input().rstrip() for _ in range(n)]))
sortbylen = sorted(words, key= lambda x: (len(x), x))

for word in sortbylen:
    print(word)
