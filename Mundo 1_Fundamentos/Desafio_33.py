n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
n3 = float(input('Digite um número: '))

if n1 > n2 and n1 > n3:
    print(f'O MAIOR valor digitado foi {n1}.')
if n1 < n2 and n1 < n3:
    print(f'O MENOR valor digitado foi {n1}.')

if n2 > n1 and n2 > n3:
    print(f'O MAIOR valor digitado foi {n2}.')
if n2 < n1 and n2 < n3:
    print(f'O MENOR valor digitado foi {n2}.')

if n3 > n2 and n3 > n1:
    print(f'O MAIOR valor digitado foi {n3}.')
if n3 < n2 and n3 < n1:
    print(f'O MENOR valor digitado foi {n3}.')
