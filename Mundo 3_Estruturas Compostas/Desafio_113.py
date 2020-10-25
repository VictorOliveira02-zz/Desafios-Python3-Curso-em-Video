def read_int(txt):
    while True:
        try:
            read = int(input(txt))
        except (ValueError, TypeError, KeyboardInterrupt):
            print('\033[1;31mError! Please, only type int number!\033[m')
            continue
        else:
            return read

def read_real(txt):
    while True:
        try:
            read = float(input(txt))
        except (ValueError, TypeError, KeyboardInterrupt):
            print('\033[1;31mError! Please, only type float number!\033[m')
            continue
        else:
            return read
        

num = read_int('Type a int number: ')
num_real = read_real('Type a real number: ')
print(f'\033[1;32mYOU TYPE INT NUMBER {num}\033[m.')
print(f'\033[1;32mYOU TYPE FLOAT NUMBER {num_real}\033[m.')
