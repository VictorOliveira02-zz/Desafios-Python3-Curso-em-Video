n = input('Digite seu nome completo:')

print('\nAnalisando seu nome..\n')
print(f'Seu nome em minusculo é {n.lower()}')
print(f'Seu nome em maiusculo é {n.upper()}')
print(f'Seu nome tem {len(n) - n.count(" ")} letras ao todo')
s = n.split()
a = s[0]
print(f'Seu primeiro nome tem {len(a)} letras')
