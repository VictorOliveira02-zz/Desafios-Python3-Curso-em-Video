from math import sqrt
co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))

hip = (co**2) + (ca**2)

print(f'O valor da hipotenusa é {sqrt(hip)}')
