print('='*40)
print(f'{" CAIXA ELETRÔNICO ": ^40}')
print('='*40)
saque = int(input('DIGITE O VALOR DE SAQUE (R$): '))
total = saque
ced = 50
contaced = 0
while True:
    if total >= ced:
        total -= ced
        contaced += 1
    else:
        if contaced > 0:
            print(f'TOTAL DE {contaced} CÉDULAS DE R$ {ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        contaced = 0
        if total == 0:
            break
print('='*40)
print(f'{" MUITO OBRIGADO, VOLTE SEMPRE! ": ^40}')
