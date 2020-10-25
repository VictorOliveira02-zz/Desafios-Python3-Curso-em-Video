from random import randint
from time import sleep
from pygame import mixer
mixer.init()
mixer.music.load('C:/Users/Cleide/Music/Music/Sample Music/Kalimba.mp3')
mixer.music.play()

print(f'\n{" PAR OU ÍMPAR GAME ":=^40}\n')

np = randint(1, 10)
soma = conta = 0

while True:
    nj = int(input('\nDIGITE UM VALOR: '))
    pi = input('VOCÊ QUER SER PAR OU ÍMPAR [P/Í]?: ').upper()[0].strip()
    print('\nO QUE SERÁ QUE ELE VAI JOGAR...')
    sleep(2)
    soma = np + nj
    conta = conta + 1
    if soma % 2 == 0 and pi == 'P':
        print('\nSHOW, VOCÊ VENCEU!')
        pi = 'PAR'
    elif soma % 2 != 0 and pi == 'I':
        print('\nSHOW, VOCÊ VENCEU!')
        pi = 'ÍMPAR'
    elif soma % 2 == 0 and pi == 'I':
        print('\nEITA, O COMPUTADOR VENCEU!')
        pi = 'PAR'
        print(f'VOCÊS JOGARAM {conta} VEZ(ES).')
    else:
        pi = 'ÍMPAR'
        print('\nEITA, O COMPUTADOR VENCEU!')
        print(f'VOCÊS JOGARAM {conta} VEZ(ES).')
    print(f'\nO COMPUTADOR PENSOU {np} E VOCÊ {nj}.SOMANDO {soma} DEU {pi}.\n')
    print('-'*50)

        
        


