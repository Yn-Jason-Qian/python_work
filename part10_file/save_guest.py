file_name = 'guests.txt'
welcome_word = 'Welcome to here, '
with open(file_name, 'w') as file_object:
    while True:
        guest_name = input('Please input guest name:')
        if guest_name == 'over':
            break
        else:
            file_object.write(welcome_word + guest_name + '.\n')
            print(welcome_word + guest_name + '.')

