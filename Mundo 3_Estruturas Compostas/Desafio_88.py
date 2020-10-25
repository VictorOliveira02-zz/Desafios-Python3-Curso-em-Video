from time import sleep
from random import randint

n = 0
num = []

while n != -1:
    print(f'\n{" JOGO DA MEGA SENA ":=^40}')
    n = int(input("\nQuantos jogos você quer sortear ? /-1 para SAIR: "))
    for c in range(0,n):
        num = [randint(1,60)]
        while len(num) != 6:
            r = randint(1,60)
            if r not in num:
                    num.append(r)
        sleep(0.9)
        print(f'JOGO {c+1} -> {sorted(num)}')
    print(f'\n{" BOA SORTE! ":=^40}\n')
