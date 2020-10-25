print(f'\n{" PAPELARIA LECTOR ":=^34}\n')
produtos = ('CANETA BIC..............R$ 1,50'
            '\nLAPIS B2................R$ 0,50'
            '\nCADERNO.................R$ 4,50'
            '\nTINTA 250 ml............R$ 3,50'
            '\nRÉGUA...................R$ 2,00'
            '\nBORRACHA................R$ 0,50'
            '\nMOCHILA...............R$ 100,00'
            '\nAPONTADOR...............R$ 1,50'
            '\nCOLA BRANCA.............R$ 2,50'
            '\nCOLA BASTÃO.............R$ 3,50'
            '\nPEN DRIVE..............R$ 30,00\n')
print(produtos)
print('='*33)

lista = ('CANETA BIC','1,50',
        'LAPIS B2','0,50',
        'CADERNO','4,50',
        'TINTA 250 ml','3,50',
        'RÉGUA','2,00',
        'BORRACHA','0,50',
        'MOCHILA','100,00',
        'APONTADOR','1,50',
        'COLA BRANCA','2,50',
        'COLA BASTÃO','3,50',
        'PEN DRIVE','30,00')
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end=' ')
    else:
        print(f' R$ {lista[pos]: <7}')
