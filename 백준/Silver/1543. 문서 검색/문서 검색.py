text = input()
search = input()

ans = 0
i=0
while i <= len(text) - len(search):
    if text[i:i+len(search)] == search:
        ans += 1
        i += len(search)
    else:
        i += 1
print(ans)