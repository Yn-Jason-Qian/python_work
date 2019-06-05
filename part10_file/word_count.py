def divide():
    print('Please input two number.')
    print('This will give the result of division.')
    while True:
        first = input('Please input first number:')
        if first == 'q':
            break
        second = input('Please input second number:')
        if second == 'q':
            break
        try:
            first_num = int(first)
            second_num = int(second)
            print(first_num/second_num)
        except ValueError:
            print('Please input integer number!')
            print('')
        except ZeroDivisionError:
            print('Second number can not be zero!')
            print('')
divide()
