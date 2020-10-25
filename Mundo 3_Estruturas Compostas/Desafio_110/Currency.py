def increase(n):
    porcent = n * 0.10
    return f'{n + porcent:.2f}'.replace('.', ',')

def decrease(n):
    porcent = n * 0.15
    return f'{n - porcent:.2f}'.replace('.', ',')

def double(n):
    return f'{n * 2:.2f}'.replace('.', ',')

def half(n):
    return f'{n / 2:.2f}'.replace('.', ',')

def Currency(n=0):
    return f'{n:.2f}'.replace('.', ',')

def Resume(n):
    print('-' * 40)
    print('RESUME VALUES'.center(40))
    print('-' * 40)
    print(f'Price: \t\tR$ {Currency(n)}')
    print(f'Sum 10%: \tR$ {increase(n)}')
    print(f'Subtra 15%: \tR$ {decrease(n)}')
    print(f'Double: \tR$ {double(n)}')
    print(f'Half: \t\tR$ {half(n)}')
    print('-' * 40)
