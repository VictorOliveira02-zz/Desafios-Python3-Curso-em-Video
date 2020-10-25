def read_int(number):
    while not number.isnumeric():
        number = input("\033[1;31mERROR! PLEASE, TYPE ONLY NUMBERS!:\033[m ")
    return f'\033[1;32mYOU TYPE NUMBER {number}\033[m.'
        

number = input('Type a number: ')
print(read_int(number))
