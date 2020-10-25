soma = 0
conta = 0
maior = 0
for c in range(1, 5):
    print(f'\n----- {c}° PESSOA -----\n')
    nome = input('NOME: ').title().strip()
    idade = int(input('\nIDADE: '))
    sexo = input('\nSEXO [F\M]: ').upper().strip()
    soma = soma + idade
    if sexo == 'F' and idade < 20:
        conta = conta + 1
    if sexo == 'M' and c == 1:
        maior = idade
    else:
        if idade > maior:
            maior = idade
    if idade == maior and sexo == 'M':
        velho = nome
    
print(f'\nA MÉDIA DE IDADE DO GRUPO FOI DE {soma/4} ANOS.')
print(f'{conta} MULHER(ES) TEM MENOS DE 20 ANOS.')
print(f'O HOMEM MAIS VELHO SE CHAMA {velho} E TEM {maior} ANOS.')
