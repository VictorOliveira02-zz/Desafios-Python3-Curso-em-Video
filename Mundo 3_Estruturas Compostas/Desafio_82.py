lista = []
pares = []
ímpar = []
while True:
    n = int(input('Digite um valor ou ZERO para SAIR: '))
    if n == 0:
        break
    lista.append(n)
    lista.sort()
    if n % 2 == 0:
        pares.append(n)
        pares.sort()
    else:
        ímpar.append(n)
        ímpar.sort()

print(f'LISTA DIGITADA -> {lista}')
print(f'NUMEROS PARES -> {pares}')    
print(f'NUMEROS ÍMPARES -> {ímpar}')
