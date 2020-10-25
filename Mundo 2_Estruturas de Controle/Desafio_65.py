n = int(input('Digite um número: '))
op = input('Quer continuar?[S/N]: ').upper()[0].strip()

maior = menor = n
soma = conta = 0

while op != 'N':
    n = int(input('Digite um número: '))
    op = input('Quer continuar?[S/N]: ').upper()[0].strip()
    conta = conta + 1
    soma = soma + n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    
print(f'A MÉDIA DOS NÚMEROS É {soma/conta}.')
print(f'O MAIOR VALOR É {maior} E O MENOR {menor}.')
