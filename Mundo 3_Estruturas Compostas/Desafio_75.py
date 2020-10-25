tupla = int(input('Digite um numero: ')),int(input('Digite um numero: ')),int(input('Digite um numero: ')),int(input('Digite um numero: '))
conta = 0
print(f'Voce digitou os valores {tupla}')
print(f'O valor 9 foi digitado {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 foi digitado na posição {tupla.index(3)}')
for n in tupla:
    if n % 2 == 0:
        conta += 1
print(f'{conta} valores são pares')
        
    
