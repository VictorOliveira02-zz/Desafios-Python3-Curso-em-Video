jogadores = []
jogador = {}
repetir = 'S'
num = 0
while repetir == 'S':
    print('-' * 40)
    while True:
        jogador['NOME'] = input('Nome do jogador: ').capitalize().strip()
        if not jogador['NOME'].isnumeric():
            break
        print('Erro! Digite um nome válido!')
    partidas = int(input(f'Quantas partidas {jogador["NOME"]} jogou? '))
    jogador['GOLS'] = [int(input(f'   Gols {n + 1}ª partida: ')) for n in range(partidas)]
    jogador['TOTAL'] = sum(jogador['GOLS'])
    jogador['Média'] = round(jogador['TOTAL'] / partidas, 2)
    jogadores.append(jogador.copy())
    print('-' * 40)
    repetir = ''
    while len(repetir) != 1 or repetir not in 'SN':
        repetir = input('Cadastrar outro jogador? [S/N] ').upper().strip()
        if len(repetir) != 1 or repetir not in 'SN':
            print('Digite S para Sim e N para Não.')
print('-' * 30)
print('| CÓD ', end=''), [print(f'| {k:^10} ', end='') for k in jogador.keys()], print('|')
print('-' * 59)
for n, j in enumerate(jogadores):
    print(f'| {n:^3} | {j["NOME"]:^10} | {(" ".join(str(g) for g in j["GOLS"])):^10} | {j["TOTAL"]:^10} | {j["Média"]:^10} |')
while num != 999:
    print('-' * 59)
    num = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if num in range(len(jogadores)):
        print(f'\n-- LEVANTAMENTO DO JOGADOR {jogadores[num]["NOME"]}:')
        for n, gol in enumerate(jogadores[num]['GOLS'], 1):
            print(f'   No {n}º jogo fez {gol} gol(s).')
    elif num != 999:
        print(f'\nERRO! Não existe jogador com código {num}! Tente novamente.')
print('\n<< VOLTE SEMPRE >>')
