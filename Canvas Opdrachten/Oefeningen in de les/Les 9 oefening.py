def sum():
    total = 0
    while True:
        nextInt = input('next int: ')
        if nextInt == 'quit':
            break
        total += int(nextInt)
    print(total)
