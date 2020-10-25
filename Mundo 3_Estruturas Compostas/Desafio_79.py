lista = []
while True:
    n = int(input('Digite um valor ou zero para sair: '))
    if n not in lista:
        lista.append(n)   
    if n == 0:
        lista.pop(-1)
        break
    lista.sort()
print('-'*30)
print(f'Você digitou os valores : {lista}')
