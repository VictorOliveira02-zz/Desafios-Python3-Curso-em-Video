from datetime import date

atual = date.today().year
conta = 0
cont = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de NASC.: '))
    idade = atual - ano
    if idade < 18:
        conta = conta + 1
    else:
        cont = cont + 1
print (f'O número de pessoas menores de idade são : {conta} pessoas.')
print (f'O número de pessoas maiores de idade são : {cont} pessoas.')
    
