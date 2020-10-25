from time import sleep

alunos = [[], [], [], []]
cont = ""

while True:
    alunos[0].append(input('Nome: '))
    alunos[1].append(float(input('Nota 1: ')))
    alunos[2].append(float(input('Nota 2: ')))
    alunos[3].append((alunos[1][-1]+alunos[2][-1])/2)
    resp = input('Deseja continuar? [S/N] ')
    if resp in 'Nn':
        break
print('-='*25)
print(f'{"Nº.":<5}{"NOME":<9}{"MÉDIA":>6}')
print('-'*25)
for a in range(0, len(alunos[0])):
    print(f'{a:<5}{alunos[0][a]:<9}{alunos[3][a]:>6}')
print('-' * 30)
while True:
    novo = int(input('Mostrar a nota de qual aluno? (999 interrompe): '))
    if novo == 999:
        break
    print(f'Notas de {alunos[0][novo]} são {alunos[1][novo]} e {alunos[2][novo]}.')
    print('-' * 30)
print('Finalizando...')
sleep(1)
print('<<< Volte sempre >>>')
