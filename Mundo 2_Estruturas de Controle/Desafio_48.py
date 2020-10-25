soma = 0
conta = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        conta = conta + 1
print(f'A soma dos ímpares divisivéis por 3 é igual a {soma},sendo utilizados {conta} números.')
