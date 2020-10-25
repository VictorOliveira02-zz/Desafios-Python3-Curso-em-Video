n = float(input('Digite a distância da viagem: '))

if n <= 200:
    print(f'Por {n} KM, o preço fica {n*0.5} R$.')
else:
    print(f'Por {n} KM, o preço fica {n*0.45} R$.')
    
