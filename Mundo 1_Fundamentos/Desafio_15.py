d = float(input('Quantos dias alugados ?: '))
k = float(input('Quantos KM rodados?: '))

x = d * 60
x2 = k * 0.15

print(f'O total a pagar é R${x + x2}')
