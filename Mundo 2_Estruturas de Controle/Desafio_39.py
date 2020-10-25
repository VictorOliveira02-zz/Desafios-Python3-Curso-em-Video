from datetime import date

s = input('Digite a letra correspondente ao seu sexo ?:\n''[ M ] - MASCULINO\n''[ F ] - FEMININO\n'': ').strip().title()

if s == 'F':
    
    print('Devido ao seu sexo,não é necesario que voce se aliste obrigatoriamnete.')
else:    
    if s == 'M':
        an = int(input('Digite o ano em que você nasceu: '))
        da = an + 18
        x = date.today().year
        if da > x:
            print(f'Você ainda se alistará.Aguarde {da - x} anos.')
        elif da == x:
            print('Prepra-se soldado!Este é o ano do seu alistamento!')
        else:
            print(f'Ja se passaram {x - da} anos que você se alistou!')

