aberto = fechado = 0
expre = input('Digite a expressão: ')
lista = []

for simbo in expre:
    if simbo == '(':
        lista.append('(')
    elif simbo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
        
if len(lista) == 0:
    print('A expressão está CORRETA!')
else:
    print('A expressão está INCORRETA!')
    


    
    

