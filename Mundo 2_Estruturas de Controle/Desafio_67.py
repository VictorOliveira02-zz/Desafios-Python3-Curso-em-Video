while True:
    n = int(input('Qual tabuada vocé quer saber ?: '))
    if n < 0:
        break
    print('-'*50)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-'*50)
