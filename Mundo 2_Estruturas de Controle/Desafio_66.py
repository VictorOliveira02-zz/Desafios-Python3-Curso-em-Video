soma = conta = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    soma = soma + n
    conta = conta + 1
print(f'DOS {conta} VALORES DIGITADOS A SOMA TOTAL É {soma}.')
