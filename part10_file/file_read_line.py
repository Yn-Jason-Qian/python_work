path = 'pi_digits.txt'
with open(path) as file_object:
    for line in file_object:
        print(line.rstrip())

