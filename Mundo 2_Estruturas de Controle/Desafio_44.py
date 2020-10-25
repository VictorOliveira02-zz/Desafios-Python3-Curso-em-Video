from time import sleep
from pygame import mixer

mixer.init()
mixer.music.load('C:/Users/Cleide/Music/Music/Sample Music/Sleep Away.mp3')
mixer.music.play()

print(f'{" OLÁ, SEJA BEM-VINDO(A) ":=^40}')
print(f'{" LOJAS LECTOR ":=^40}')

valor = float(input('\nDigite o valor total da compra (R$): '))
print('\nCarregando as condiçôes de pagamento...\n')
sleep(2)
print('''Selecione a opção desejada:
      [ 1 ] - Á VISTA DINHEIRO/CHEQUE: 10% DESCONTO.
      [ 2 ] - Á VISTA NO CARTÃO: 5% DESCONTO.
      [ 3 ] - EM ATÉ 2x NO CARTÃO: PREÇO NORMAL.
      [ 4 ] - 3x OU MAIS NO CARTÃO: 20% DE JUROS.''')
opçao = input('Opção: ')

if opçao == '1':
    print(f'Valor total é de {valor-valor*0.10}R$.')
elif opçao == '2':
    print(f'Valor total é de {valor-valor*0.05}R$.')
elif opçao == '3':
    print(f'Valor total de 2 parcelas mensais de {valor/2:.2f}R$.')
elif opçao == '4':
    parcelas = int(input('Em quantas vezes deseja parcelar?: '))
    print(f'Valor total de {parcelas} parelas mensais é {((valor*0.2)+valor)/parcelas:.2f}R$.')
else:
    print('Por favor,selecione uma condição válida!\n')

print(f'{" OBRIGADO(A), VOLTE SEMPRE!":=^40}')




