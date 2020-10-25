palavra = 'MACACO','ARROZ','AZEITONA','LASANHA','PIZZA','CANETA','PARALELEPIPEDO','ONZE','FERNANDO','CAIO'
for p in palavra:
    print(f'\nNA PALAVRA {p} TEMOS AS VOGAIS ',end='')
    for letra in p:
        if letra in 'AEIOU':
            print(letra, end=' ')
