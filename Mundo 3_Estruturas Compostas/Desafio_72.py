num = 'zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte'
while True:
     n = int(input('Digite um numero de 0 a 20: '))
     if n >= 0 and n <= 20:
          break
print(f'Você digitou o numero {num[n]}')

