analise_alunos = {}
while True:
    analise_alunos['NOME'] = input("\nNOME DO ALUNO: ").title()
    analise_alunos['MÉDIA'] = float(input("MÉDIA FINAL: "))
    if analise_alunos['MÉDIA'] >= 7:
        print('-'*25)
        print(f'ALUNO: {analise_alunos["NOME"]}')
        print(f'MÉDIA FINAL: {analise_alunos["MÉDIA"]}')
        print(f'SITUAÇÃO: \033[1;32mAPROVADO!\033[m')
    else:
        print('-'*25)
        print(f'ALUNO: {analise_alunos["NOME"]}')
        print(f'MÉDIA FINAL: {analise_alunos["MÉDIA"]}')
        print(f'SITUAÇÃO: \033[1;31mREPROVADO!\033[m')
    resp = input('\nDESEJA VERIFICAR A SITUAÇÃO DE OUTROS ALUNO [S/N]: ').upper()
    if 'S' not in resp:
        break
