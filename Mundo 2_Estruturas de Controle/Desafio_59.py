n1 = float(input('\nPRIMEIRO VALOR: '))
n2 = float(input('SEGUNDO VALOR: '))

print('\nOQUE DESEJA FAZER?')
menu = int(input('[ 1 ] - SOMAR\n[ 2 ] - MULTIPLICAR\n[ 3 ] - SUBTRAIR\n[ 4 ] - DIVIDIR\n[ 5 ] - MAIOR OU MENOR\n[ 6 ] - NOVOS NÚMEROS\n[ 7 ] - SAIR\n-> QUAL SUA OPÇÃO: '))

while menu != 7:
    if menu == 1:
        print(f'\nA SOMA DE {n1} + {n2} = {n1+n2}\n')
        menu = int(input('[ 1 ] - SOMAR\n[ 2 ] - MULTIPLICAR\n[ 3 ] - SUBTRAIR\n[ 4 ] - DIVIDIR\n[ 5 ] - MAIOR OU MENOR\n[ 6 ] - NOVOS NÚMEROS\n[ 7 ] - SAIR\n-> QUAL SUA OPÇÃO: '))
    elif menu == 2:
        print(f'\nA MULTIPLICAÇÃO DE {n1} x {n2} = {n1*n2}\n')
        menu = int(input('[ 1 ] - SOMAR\n[ 2 ] - MULTIPLICAR\n[ 3 ] - SUBTRAIR\n[ 4 ] - DIVIDIR\n[ 5 ] - MAIOR OU MENOR\n[ 6 ] - NOVOS NÚMEROS\n[ 7 ] - SAIR\n-> QUAL SUA OPÇÃO: '))
    elif menu == 3:
        print(f'\nA SUBTRAÇÃO DE {n1} - {n2} = {n1-n2}\n')
        menu = int(input('[ 1 ] - SOMAR\n[ 2 ] - MULTIPLICAR\n[ 3 ] - SUBTRAIR\n[ 4 ] - DIVIDIR\n[ 5 ] - MAIOR OU MENOR\n[ 6 ] - NOVOS NÚMEROS\n[ 7 ] - SAIR\n-> QUAL SUA OPÇÃO: '))
    elif menu == 4:
        if n2 == 0:
            print('O SEGUNDO VALOR NÃO PODE SER ZERO!')
            n2 = float(input('SEGUNDO VALOR: '))
        print(f'\nA DIVISÃO DE {n1} / {n2} = {n1/n2}\n')
        menu = int(input('[ 1 ] - SOMAR\n[ 2 ] - MULTIPLICAR\n[ 3 ] - SUBTRAIR\n[ 4 ] - DIVIDIR\n[ 5 ] - MAIOR OU MENOR\n[ 6 ] - NOVOS NÚMEROS\n[ 7 ] - SAIR\n-> QUAL SUA OPÇÃO: '))
    elif menu == 5:
        if n1 > n2:
            print(f'\n{n1} > {n2}\n')
            menu = int(input('[ 1 ] - SOMAR\n[ 2 ] - MULTIPLICAR\n[ 3 ] - SUBTRAIR\n[ 4 ] - DIVIDIR\n[ 5 ] - MAIOR OU MENOR\n[ 6 ] - NOVOS NÚMEROS\n[ 7 ] - SAIR\n-> QUAL SUA OPÇÃO: '))
        elif n2 > n1:
            print(f'\n{n2} > {n1}\n')
            menu = int(input('[ 1 ] - SOMAR\n[ 2 ] - MULTIPLICAR\n[ 3 ] - SUBTRAIR\n[ 4 ] - DIVIDIR\n[ 5 ] - MAIOR OU MENOR\n[ 6 ] - NOVOS NÚMEROS\n[ 7 ] - SAIR\n-> QUAL SUA OPÇÃO: '))
        else:
            print(f'\n{n1} = {n2}\n')
            menu = int(input('[ 1 ] - SOMAR\n[ 2 ] - MULTIPLICAR\n[ 3 ] - SUBTRAIR\n[ 4 ] - DIVIDIR\n[ 5 ] - MAIOR OU MENOR\n[ 6 ] - NOVOS NÚMEROS\n[ 7 ] - SAIR\n-> QUAL SUA OPÇÃO: '))
    elif menu == 6:
        n1 = float(input('\nPRIMEIRO VALOR: '))
        n2 = float(input('SEGUNDO VALOR: '))
        menu = int(input('[ 1 ] - SOMAR\n[ 2 ] - MULTIPLICAR\n[ 3 ] - SUBTRAIR\n[ 4 ] - DIVIDIR\n[ 5 ] - MAIOR OU MENOR\n[ 6 ] - NOVOS NÚMEROS\n[ 7 ] - SAIR\n-> QUAL SUA OPÇÃO: '))
    else:
        print('\nPOR FAVOR, DIGITE UMA OPÇÃO VÁLIDA!\n')
        menu = int(input('[ 1 ] - SOMAR\n[ 2 ] - MULTIPLICAR\n[ 3 ] - SUBTRAIR\n[ 4 ] - DIVIDIR\n[ 5 ] - MAIOR OU MENOR\n[ 6 ] - NOVOS NÚMEROS\n[ 7 ] - SAIR\n-> QUAL SUA OPÇÃO: '))
        
