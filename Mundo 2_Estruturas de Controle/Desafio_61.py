print(f'\n{" 10 TERMOS DE UMA P.A ":=^40}\n')

a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

conta = 1
termo = a1

while conta <= 10:
    termo = termo + r
    conta = conta + 1
    print(termo,end=' ')
