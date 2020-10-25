from datetime import date

nasc = int(input('Digite o ano de Nasc. do(a) atleta: '))

x = date.today().year
idade = x - nasc

if idade <= 9:
    print(f'O atleta tem {idade} anos e é classificado como MIRIM')
elif idade <= 14 and idade >= 10:
    print(f'O atleta tem {idade} anos e é classificado como INFANTIL')
elif idade <= 19 and idade >= 15:
    print(f'O atleta tem {idade} anos e é classificado como JUNIOR')
elif idade <= 25 and idade >= 20:
    print(f'O atleta tem {idade} anos e é classificado como SÊNIOR')
else:
    idade > 25
    print(f'O atleta tem {idade} anos e é classificado como MASTER')
    
