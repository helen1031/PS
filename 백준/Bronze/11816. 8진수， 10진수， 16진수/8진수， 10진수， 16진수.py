x = input()

if x[:2] == "0x":
    x = x[2:]
    x = x[::-1]
    number = 0
    for i, num in enumerate(x):
        if num in "0123456789":
            number += int(num) * (16 ** i)
        else:
            number += (ord(num) - 87) * (16 ** i)
        
elif x[0] == "0":
    x = x[1:]
    x = x[::-1]
    number = 0
    for i, num in enumerate(x):
        number += int(num) * (8 ** i)
    
else:
    number = int(x)
    
print(number)