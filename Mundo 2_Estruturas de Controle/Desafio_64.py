n = conta = soma = 0
n = int(input('Digite um valor para soma (999 para SAIR): '))
while n != 999:
    soma = soma + n
    conta = conta + 1
    n = int(input('Digite um valor para soma (999 para SAIR): '))
print(f'A SOMA DOS {conta} VALORES É IGUAL Á {soma}.')
    
    
