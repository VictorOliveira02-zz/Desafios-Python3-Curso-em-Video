from random import randint

numeros = []

def sorteia():
    for _ in range(0, 5):
        numeros.append(randint(0, 50))
    print(f'VALORES SORTEADOS: {numeros}.')
def somapar():
    soma = 0
    for v in numeros:
        if v % 2 == 0:
            soma += v
    print(f'A SOMA DOS VALORES PARES SORTEADOS É = {soma}.')

sorteia()
somapar()
