n = int(input('Digite um número: '))

cont = 0

for c in range(1,n + 1):
    if n % c == 0:
        cont = cont + 1
print(f'O número {n} foi divisivel {cont} vezes,', end=' ')
        
if  cont == 2:
    print('É PRIMO.')
else:
    print('NÃO É PRIMO.')

        
