from time import sleep
cad = conta_maior = conta_homens = conta_mulheres = conta_cad = 0

while cad != 'N':
    print('-'*40)
    print(f'{" CADASTRO DE PESSOAS ": ^40}')
    print('-'*40)
    idade = int(input('IDADE: '))
    sexo = input('SEXO [M\F]: ').upper()[0].strip()
    print('-'*40)
    cad = input('DESEJA CADASTRAR MAIS PESSOAS ?: ').upper()[0].strip()
    conta_cad += 1
    if idade > 18:
        conta_maior += 1
    if sexo == 'M':
        conta_homens += 1
    if sexo == 'F' and idade < 20:
        conta_mulheres += 1
    if cad == 'N':
        print('AGUARDE.CARREGANDO RELATORIO FINAL.')
        sleep(2)
        print(f'\nFIM. {conta_cad} PESSOAS FORAM CADASTRADAS.')
        print(f'\n{conta_maior} PESSOAS TEM IDADE ACIMA DE 18 ANOS.')
        print(f'\n{conta_homens} HOMENS FORAM CADASTRADOS.')
        print(f'\n{conta_mulheres} MULHERES TEM IDADE ABAIXO DE 20 ANOS.')
        break


    
        
    
