lista = []
while True:
    n = int(input('Digite um numero ou ZERO para SAIR: '))
    if n == 0:
        break
    lista.append(n)
    lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} valores')
print(f'Os valores digitados são -> {lista}')
if 5 in lista:
    print(f'O valor 5 está na lista!')
else:
    print('O valor 5 não foi encontrado!')
