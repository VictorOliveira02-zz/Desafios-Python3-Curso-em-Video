import Currency


n = float(input('Please, type a value (R$): '))
print(f'\nSum of 10% of R$ {Currency.Currency(n)} = R${Currency.Currency(Currency.increase(n))}')
print(f'Subtraction of 15% of R$ {Currency.Currency(n)} = R${Currency.Currency(Currency.decrease(n))}')
print(f'Double of R$ {Currency.Currency(n)} = R${Currency.Currency(Currency.double(n))}')
print(f'Half of R$ {Currency.Currency(n)} = R${Currency.Currency(Currency.half(n))}')
