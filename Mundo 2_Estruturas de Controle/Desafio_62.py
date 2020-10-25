a1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 10
while c > 0:
    print(a1, end=' ')
    a1 += razao
    c -= 1
    if c == 0:
        c = int(input('\nAcrescentar mais números na sequência: '))

