lista = []
for c in range(0,5):
    n = int(input("Digite um numero: "))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            lista.insert(pos,n)
            break
        pos += 1
print(lista)
            
