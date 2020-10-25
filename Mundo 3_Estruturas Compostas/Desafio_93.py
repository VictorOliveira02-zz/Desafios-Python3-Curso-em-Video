jogador = {}
lista_gols = []

jogador['NOME'] = (input('\nNOME: ')).title()
jogador['JOGOS'] = int(input('QUANTIDADE DE JOGOS: '))
for c in range(0, jogador['JOGOS']):
   lista_gols.append(int(input(f'GOLS NA {c+1}º PARTIDA: ')))
print('-'*30)
print(f'EM {jogador["JOGOS"]} PARTIDAS O JOGADOR {jogador["NOME"]}: ')
for pos,g in enumerate(lista_gols):
   print(f'NA {pos+1}º PARTIDA, FEZ {g} GOLS.')
print(f'SOMA TOTAL DE GOLS -> {sum(lista_gols)}.')
