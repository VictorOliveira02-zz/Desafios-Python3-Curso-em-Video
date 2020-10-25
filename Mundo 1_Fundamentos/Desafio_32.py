from datetime import date

a = int(input('Digite um ano ou digite ZERO para o atual: '))

if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'{a} É UM ANO BISSEXTO!')
else:
    print(f'{a} NÃO É UM ANO BISEXTO!')
