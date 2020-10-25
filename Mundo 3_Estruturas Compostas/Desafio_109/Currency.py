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
