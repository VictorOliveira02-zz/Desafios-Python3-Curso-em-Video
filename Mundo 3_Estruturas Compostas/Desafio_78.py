lista = []
for v in range(0,5):
    lista.append(int(input("Digite um numero: ")))
print(f'Você digitou os numeros {lista}.')
print(f'Os maiores valores digitados foram {max(lista)} e estão nas posiçôes {lista.index(max(lista))+1}')
print(f'Os menores valores digitados foram {min(lista)} e estão nas posiçôes {lista.index(min(lista))+1}')
