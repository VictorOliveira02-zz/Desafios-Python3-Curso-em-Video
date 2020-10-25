from datetime import datetime

cadastro = {}

cadastro['Nome'] = input("Nome: ").title()
cadastro['Nasc'] = int(input("Ano de Nascimento: "))
cadastro['CDT'] = int(input("Número Carteira de Trabalho ? (Digite ZERO caso não tenha): "))

data = datetime.now().year - cadastro['Nasc']

if cadastro['CDT'] == 0:
    print('-'*35)
    print(f'-> NOME: {cadastro["Nome"]}')
    print(f'-> IDADE: {data} ANOS')

elif cadastro['CDT'] != 0:
    cadastro['Contra'] = int(input("Ano de contração: "))
    cadastro['Salário'] = float(input("Salário (R$): "))
    aposenta = cadastro['Contra'] - cadastro['Nasc'] 
    print('-'*35)
    print(f'-> NOME: {cadastro["Nome"]}')
    print(f'-> IDADE: {data} ANOS')
    print(f'-> CARTEIRA DE TRABALHO: {cadastro["Contra"]}')
    print(f'-> DATA DE CONTRAÇÃO: {cadastro["CDT"]}')
    print(f'-> SALÁRIO: {cadastro["Salário"]} R$')
    print(f'-> IDADE DE APOSENTADORIA: {aposenta+35} ANOS')
    print(f'-> TEMPO RESTANTE PARA TRABALHAR: {(aposenta+35)-data} ANOS')
