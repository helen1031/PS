import sys
input = sys.stdin.readline

n = int(input())
dic = {}
for _ in range(n):
    word = list(input().strip())
    for i in range(len(word)):
        if word[i] not in dic:
            dic[word[i]] = 10 ** (len(word) - 1 - i)
        else:
            dic[word[i]] += 10 ** (len(word) - 1 - i)
            
sorted_dic = sorted(dic.items(), key = lambda item:item[1], reverse=True)
num = 9
ans = 0
for item in sorted_dic:
    key, value = item
    ans += value * num
    num -= 1
    
print(ans)
    