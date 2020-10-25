import Currency


n = float(input('Please, type a value (R$): '))
print(f'\nSum of 10% of R$ {n} = R${Currency.increase(n)}')
print(f'Subtraction of 15% of R$ {n} = R${Currency.decrease(n)}')
print(f'Double of R$ {n} = R${Currency.double(n)}')
print(f'Half of R$ {n} = R${Currency.half(n)}')
