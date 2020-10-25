soma = conta_mil = mais_barato = conta = 0
prod_barato = ' '
while True:
    print('-'*50)
    print(f'{" LOJAS LECTOR ": ^40}')
    print('-'*50)
    nome = input('NOME DO PRODUTO: ').upper().strip()
    preço = float(input('PREÇO (R$): '))
    soma += preço
    conta += 1
    if preço > 1000:
        conta_mil += 1
    if conta == 1:
        mais_barato = preço
        prod_barato = nome   
    else:
        if preço < mais_barato:
            mais_barato = preço
            prod_barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = input('DESEJA CONTINUAR [S/N]? : ').upper()[0].strip()
    if resp == 'N':
        break
        
print(f'{" FIM DO PROGRAMA ":-^50}')
print(f'A SOMA TOTAL DOS PRODUTOS É DE R$ {soma}.')
print(f'{conta_mil} PRODUTOS CUSTAM MAIS DE R$ 1000,00.')
print(f'O PRODUTO MAIS BARATO CUSTA R$ {mais_barato} - {prod_barato}.')

