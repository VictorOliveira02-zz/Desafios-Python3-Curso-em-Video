from math import factorial

n = int(input('Digite um número para calcular o FATORIAL: '))
c = n
f = 1

while c > 0:
    print(f'{c}',end='')
    print(' x ' if c > 1 else ' = ',end='')
    c = c - 1
    f = f * c
print(factorial(n))
