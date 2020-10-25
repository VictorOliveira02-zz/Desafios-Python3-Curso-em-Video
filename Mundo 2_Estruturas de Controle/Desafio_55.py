maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'PESO da {p}° pessoa. (KG): '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O MAIOR PESO FOI DE {maior}KG')
print(f'O MENOR PESO FOI DE {menor}KG')
