cadastro = []
lista = []
peso_leve = peso_pesado = 0
while True:
    lista.append(input("\nDigite o nome do cliente: "))
    lista.append(float(input("Digite o peso do cliente (Kg): ")))
    if len(cadastro) == 0:
        peso_leve = peso_pesado = lista[1]
    else:
        if lista[1] > peso_pesado:
            peso_pesado = lista[1]
        if lista[1] < peso_leve:
            peso_leve = lista[1]
    cadastro.append(lista[:])
    lista.clear()
    resp = input("Deseja continuar ?[S/N]: ").upper()
    if "N" in resp:
        break
    
print(f'\n{len(cadastro)} PESSOAS FORAM CADASTRADAS.')
print(f'MAIOR PESO: {peso_pesado} Kg')
print(f'MENOR PESO: {peso_leve} Kg\n')

















