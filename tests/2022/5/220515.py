# Convert hex to num

# def hextonum1(num: str):
#     a = hex(num)
#     print(int(a))

# hextonum1(input('hex to num: '))

def hextonum2(num: str):
    dec = 0
    x: int
    for i, char in enumerate(num):
        char = char.lower()
        match char:
            case 'a':
                x = 10
            case 'b':
                x = 11
            case 'c':
                x = 12
            case 'd':
                x = 13
            case 'e':
                x = 14
            case 'f':
                x = 15
            case _:
                x = int(char)
        dec += x*16**i
    print(dec)

def hextonum3(hex: str):
    # conversion
    dec = int(hex, 16)
    
    print('Value in hexadecimal:', hex)
    print('Value in decimal:', dec)

print('OI')
hextonum3(input('hex to num: '))
#input()