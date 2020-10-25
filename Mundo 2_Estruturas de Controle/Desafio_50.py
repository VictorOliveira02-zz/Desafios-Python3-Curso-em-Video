soma = 0
conta = 0
for c in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma = soma + n
        conta = conta + 1
print(f'A soma de {conta} números pares é igual a {soma}.')
