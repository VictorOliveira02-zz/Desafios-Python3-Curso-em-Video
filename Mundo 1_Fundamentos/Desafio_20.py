from random import shuffle
a1 = input('Digite o nome do aluno:')
a2 = input('Digite o nome do aluno:') 
a3 = input('Digite o nome do aluno:') 
a4 = input('Digite o nome do aluno:')
alunos = [a1, a2, a3, a4]
shuffle(alunos)

print(f'A apresentação será na seguinte ordem : {alunos}')
