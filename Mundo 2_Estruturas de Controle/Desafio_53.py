frase = input('Qual a frase?: ').upper().strip()

frase = frase.split()
jfrase = ''.join(frase)
inverso = ''

for letra in range(len(jfrase) - 1, -1, -1):
    inverso += jfrase[letra]
if inverso == jfrase:
    print('PALÍNDROMO')
else:
    print('NUM É PALIN')
