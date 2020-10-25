n = int(input('Digite o valor que deseja converter: '))
print('¨¨'*30)
opcoes = int(input('Para qual base converter ?\n''[ 1 ] - BINÁRIO\n''[ 2 ] - OCTAL\n''[ 3 ] - HEXADECIMAL\n''Sua opção: '))

if opcoes == 1:
    print(f'O número {n} em BINÁRIO é {bin(n)[2:]}')
elif opcoes == 2:
    print(f'O número {n} em OCTAL é {oct(n)[2:]}')
elif opcoes == 3:
    print (f'O número {n} em HEXADECIMAL é {hex(n)[2:]}')
else:
    print('Esta opção não existe, selecione uma válida.')
