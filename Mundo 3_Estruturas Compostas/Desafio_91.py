from random import randint
from time import sleep
from operator import itemgetter

jogada = {}
ranking = []

jogada['Jogador 1'] = randint(1,6)
jogada['Jogador 2'] = randint(1,6)
jogada['Jogador 3'] = randint(1,6)
jogada['Jogador 4'] = randint(1,6)

print('\nAO SINAL,CADA JOGADOR DEVE JOGAR SEU DADO...')
print('PREPARAR....')
sleep(3)
print('\nAPONTAR....')
sleep(2)
print('\nJÁ !!!\n')
sleep(1)
for k,v in jogada.items():
    print(f'{k} -> {v}')
print(f'\n{" RANKING DOS JOGADORES ":-^40}\n')
ranking = sorted(jogada.items(), key=itemgetter(1), reverse=True)
for pos,player in enumerate(ranking):
        print(f'{pos+1}º LUGAR -> {player[0]} : {player[1]}')
        sleep(1)
