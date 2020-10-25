print(f'\n{" 10 TERMOS DE UMA P.A ":=^40}\n')

a1 = int(input('Digite o Primeiro Termo: '))
r = int(input('Digite a Razão: '))

an = a1 +(11 - 1) * r
for c in range(a1, an, r):
    print(c, end=' -> ')
print('FIM!')
