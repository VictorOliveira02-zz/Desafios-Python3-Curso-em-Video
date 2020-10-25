from time import sleep

def maior(*num):
    print('-'*50)
    sleep(1)
    print(f'-> Valores informados: {num}')
    print(f'-> FORAM LIDOS {len(num)} VALORES')
    print(f'-> MAIOR VALOR INFORMADO: {max(num)}')


maior(1,2,3,4,5,6,7,8,9,10,11)
maior(2,3,4,5,6,7,8)
maior(4,5)
maior(5,9,8,7,6)
