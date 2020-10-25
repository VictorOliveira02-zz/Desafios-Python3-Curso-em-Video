n1 = float(input('Digite a P1: '))
n2 = float(input('Digite a P2: '))

M = (n1+n2)/2

if M > 7:
    print(f'Aluno APROVADO com média {M}')
elif 5 >= M or M < 6.75:
    print(f'Aluno em RECUPERAÇÃO com média {M}')
else:
    print(f'Aluno REPROVADO com média {M}')
