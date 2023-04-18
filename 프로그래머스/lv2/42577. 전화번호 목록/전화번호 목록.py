def solution(phone_book):
    phone_book.sort(key = lambda x:len(x))
    phone_book.sort()
    
    current = phone_book[0]
    for i in range(1, len(phone_book)):
        compare = phone_book[i]
        if current == compare[:len(current)]:
            return False
        current = compare
    
    return True
    