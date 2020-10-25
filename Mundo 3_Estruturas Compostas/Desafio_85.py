lista = [[], []]
valor = 0

for c in range(0,7):
    valor = int(input(f'Digite o {c+1}º valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

print(f'\nPARES -> {sorted(lista[0])}')
print(F'ÍMPARES -> {sorted(lista[1])}')  
