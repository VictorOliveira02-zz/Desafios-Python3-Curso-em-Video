import sys
from time import sleep

sys.path.append('C:\\Users\\victo\\Desktop\\Victor\\Programação\\Linguagem Python\\Programas Victor - Curso em Video\\Desafio_115\\lib')
from Menu import *

while True:
    option = main('MENU PRINCIPAL')
    new_file(0)
    if option == 1:
        print('[ 1 ] - Show Registered People.')
        files(1)
    elif option == 2:
        print('[ 2 ] - Register New People.')
        name = input('Enter name: ').title()
        age = read_int('Enter age: ')
        add_file(name, age)
    elif option == 3:
        print('[ 3 ] - Exit.')
        print('-'*40)
        print('BYE, THANKS FOR USING.'.center(40))
        print('-'*40)
        break
    else:
        print('\033[1;31mError! Please, type a valid option.\033[m')
    sleep(2)
