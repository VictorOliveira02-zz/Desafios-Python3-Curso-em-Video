import random
from time import sleep

a = random.randint(0, 5)

print('----START GAME----')
n = int(input('De 0 a 5, qual o computador pensou ?: '))
print('HMM DEIXA EU VER...')
sleep(3)

if a == n:
    print('Acertou!Você venceu!!')
else:
    print(f'Errou!O computador pensou em {a}.COMPUTADOR VENCEU!')
    
print('----END GAME-----')
