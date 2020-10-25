v = float(input('Qual foi a velocidade do carro ?: '))

mm = v - 80
m = 7 * mm

if v >= 80:
    print(f'Você foi multado por alta velocidade. A multa corresponde a {m} R$.')
else:
    print('Velocidade correta!')
