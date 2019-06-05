file_name = 'pi_million_digits.txt'
with open(file_name) as file_objects:
    lines = file_objects.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input('Enter your birthday, in the form yymmdd: ')

if birthday in pi_string:
    print('Your birthday appears in the first million digits of pi!')
else:
    print('Your birthday does not appear in the first million digits of pi.')
