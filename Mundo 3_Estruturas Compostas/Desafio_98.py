from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if inicio < fim:
        fim += 1
    else:
        fim -= 1
        if passo > 0:
            passo = passo*(-1)
    print(f'CONTAGEM: ')
    for c in range(inicio, fim, passo):
        print(f'{c} ', end='-> ')
        sleep(0.5)
    print('FIM!')
    print('-'*60)


contador(1, 10,1)
contador(10, -1, -2)
print('Agora é sua vez de personalizar!')
contador(int(input('INICIO: ')), int(input('FIM: ')), int(input('PASSO: ')))
