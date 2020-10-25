cadastro = {}
lista_cadastro = []
lista_mulheres = []
lista_idade_media = []
conta_cadastro = soma = 0

while True:
    cadastro['Nome'] = input('\nDigite NOME: ').title()
    cadastro['Idade'] = float(input('Digite IDADE: '))
    soma += cadastro['Idade']
    cadastro['Sexo'] = input('Digite SEXO [M/F]: ').upper()[0]
    while cadastro['Sexo'] not in 'MF':
        cadastro['Sexo'] = input('Erro! Digite SEXO [M/F]: ').upper()[0]
    if cadastro['Sexo'] == 'F':
        lista_mulheres.append(cadastro['Nome'])
    lista_cadastro.append(cadastro.copy())
    conta_cadastro += 1
    resp = input('Deseja continuar ? [S/N]: ').upper()[0]
    while resp not in 'SN':
        resp = input('Erro! Deseja continuar ? [S/N]: ').upper()[0]
    if 'N' in resp:
        break

print('-'*45)
print(f'TOTAL DE PESSOAS CADASTRADAS: {conta_cadastro}')
print(f'MÉDIA DE IDADE CADASTRADA: {soma/conta_cadastro:.2f}')
print(f'MULHERES CADASTRADAS: {lista_mulheres}')
print(f'PESSOAS CADASTRADAS COM IDADE ACIMA DA MÉDIA:')
for pessoa in lista_cadastro:
    if pessoa['Idade'] > soma/conta_cadastro:
        for k,v in pessoa.items():
            print(f'{k} = {v}')
        print()
 