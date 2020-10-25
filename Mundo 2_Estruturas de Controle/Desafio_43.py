peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))

IMC = peso/(altura**2)

if IMC < 18.5:
    print(f'Você está ABAIXO DO PESO, seu IMC é {IMC:.1f}')
elif IMC < 25:
    print(f'Você está no PESO IDEAL, seu IMC é {IMC:.1f}')
elif IMC < 30:
    print(f'Você está com SOBREPESO, seu IMC é {IMC:.1f}')
elif IMC < 40:
    print(f'Você está com OBESIDADE, seu IMC é {IMC:.1f}')
else:
    IMC > 40
    print(f'Você está em OBESIDADE MÓRBIDA, seu IMC é {IMC:.1f}')
