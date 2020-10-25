a = float(input('Valor da primeira reta: '))
b = float(input('Valor da segunda reta: '))
c = float(input('Valor da terceira reta: '))

if (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
    print('Com essas medidas o triangulo pode ser feito')
    if a == b == c:
        print('Este triangulo é EQUILÁTERO')
    if a != b != c:
        print('Este triangulo é ESCALENO')
    if a == b != c or c == b != a or a == c != b:
        print('Este triangulo é ISÓSCELES')
else:
    print('Com essas medidas o triangulo não pode ser feito')
