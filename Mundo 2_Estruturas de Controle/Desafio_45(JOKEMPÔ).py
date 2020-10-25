from random import choice
from time import sleep
from pygame import mixer

mixer.init()
mixer.music.load('C:/Users/Cleide/Music/Sample Music/Kalimba.mp3')
mixer.music.play()

print(f'\n{" JOKEMPÔ GAME ":=^40}\n')

opçoes = int(input('''Sua opçôes:
[ 1 ] - PEDRA
[ 2 ] - PAPEL
[ 3 ] - TESOURA
QUAL SUA JOGADA ? : '''))

print('-='*20)
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PÔ !!!')
print('-='*20)

lista = ['PEDRA', 'PAPEL', 'TESOURA']
PC = choice(lista)

if opçoes == 1:
    print(f'''COMPUTADOR JOGOU {PC}.
VOCÊ JOGOU PEDRA.''')
    if PC == 'PEDRA':
        print('EMPATOU!!')
    if PC == 'PAPEL':
        print('COMPUTADOR VENCEU!!')
    if PC == 'TESOURA':
        print('VOCÊ VENCEU!!')
elif opçoes == 2:
    print(f'''COMPUTADOR JOGOU {PC}.
VOCÊ JOGOU PAPEL.''')
    if PC == 'PAPEL':
        print('EMPATOU!!')
    if PC == 'TESOURA':
        print('COMPUTADOR VENCEU!!')
    if PC == 'PEDRA':
        print('VOCÊ VENCEU!!')
elif opçoes == 3:
    print(f'''COMPUTADOR JOGOU {PC}.
VOCÊ JOGOU TESOURA.''')
    if PC == 'TESOURA':
        print('EMPATOU!!')
    if PC == 'PEDRA':
        print('COMPUTADOR VENCEU!!')
    if PC == 'PAPEL':
        print('VOCÊ VENCEU!!')
else:
    print('ESCOLHA UMA DAS OPÇÕES VÁLIDAS PARA JOGAR!')


