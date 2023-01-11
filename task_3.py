n = int(input('Write a number: '))

max = n % 10
while True:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    elif n > 9:
        continue
    else:
        print(f'Maximum Number: {max}')
        break