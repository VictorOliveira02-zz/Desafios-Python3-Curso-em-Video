sexo = input('POR FAVOR, DIGITE SEU SEXO [M/F]: ').upper()[0].strip()

if sexo == 'M' or sexo == 'F':
        print('SEXO REGISTRADO COM SUCESSO!')

while sexo != 'F' and sexo != 'M':
    sexo = input('POR FAVOR,DIGITE CORRETAMENTE SEU SEXO [M/F]: ').upper()[0].strip()
    if sexo == 'M' or sexo == 'F':
        print('SEXO REGISTRADO COM SUCESSO!')
