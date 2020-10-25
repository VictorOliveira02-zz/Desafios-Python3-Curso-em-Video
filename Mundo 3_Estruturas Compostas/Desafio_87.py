matriz = []
soma = maior = 0

for c in range(0,9):
    matriz.append(int(input(f'Digite o {c+1}º valor: ')))
for v in matriz:
    if v % 2 == 0:
        soma += v

print(f'\n[{matriz[0]:^5}][{matriz[1]:^5}][{matriz[2]:^5}]\n[{matriz[3]:^5}][{matriz[4]:^5}][{matriz[5]:^5}]\n[{matriz[6]:^5}][{matriz[7]:^5}][{matriz[8]:^5}]')
print(f'\nA SOMA DOS VALRES PARES É = {soma}')
print(f'A SOMA DOS VALORES DA TERCEIRA COLUNA É = {matriz[2]+matriz[5]+matriz[8]}')

if matriz[3] > matriz[4] and matriz[3] > matriz [5]:
    maior = matriz[3]
else:
    if matriz[4] > matriz[3] and matriz[4] > matriz[5]:
        maior = matriz[4]
    if matriz[5] > matriz[3] and matriz[5] > matriz[4]:
        maior = matriz[5]   
print(f'O MAIOR VALOR DA SEGUNDA LINHA É = {maior}\n')
