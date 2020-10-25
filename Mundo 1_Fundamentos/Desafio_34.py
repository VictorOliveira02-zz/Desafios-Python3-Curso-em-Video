s = float(input('Digite o valor do salário: '))

if s <= 1250:
    print(f'O novo salário é de {(s*0.15)+s} R$.')
else:
    print(f'O novo salário é de {(s*0.10)+s} R$.') 
