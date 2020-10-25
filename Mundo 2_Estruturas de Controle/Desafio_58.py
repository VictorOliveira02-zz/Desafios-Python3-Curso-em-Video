import random
from time import sleep

a = random.randint(0, 10)
conta = 0

print('\n---- START DIVINATION GAME ----\n')

n = int(float(input('De 0 a 10, qual o computador pensou ?: ')))
print('HMM DEIXA EU VER...')
sleep(2)
if a == n:
    print(f'Acertou de primeira!Vocês pensaram no {a}!')
else:
    while n != a:
        conta = conta + 1
        if n > a:
            n = int(input('Menos...De 0 a 10, qual o PC pensou?: '))
            print('HMM DEIXA EU VER...')
            sleep(2)
        elif n < a:
            n = int(input('Mais...De 0 a 10, qual o PC pensou?: '))
            print('HMM DEIXA EU VER...')
            sleep(2)
    if n == a:
        print(f'Acertou com {conta} tentativas!Vocês pensaram no {a}!')

print('\n---- END GAME -----\n')
