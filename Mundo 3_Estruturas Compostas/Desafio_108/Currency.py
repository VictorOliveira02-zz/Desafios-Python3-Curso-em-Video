def increase(n):
    porcent = n * 0.10
    return n + porcent

def decrease(n):
    porcent = n * 0.15
    return n - porcent

def double(n):
    return n * 2

def half(n):
    return n / 2

def Currency(n=0):
    return f'{n:.2f}'.replace('.', ',')
    