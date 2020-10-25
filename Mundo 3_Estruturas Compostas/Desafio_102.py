def factorial(number,show=False):
    '''
    -> def factorial calculate factorial of a number.
    * Parameter number = Number for know the factorial.
    * Parameter show = Option between True and False for show the multiplications.
    * Return = Return the factorial of number
    '''
    f = 1
    for c in range(number, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ',end= '')
            else:
                print(' = ', end= '')
        f *= c
    return f
   

number = int(input('Type a number: '))
print(factorial(number,show=True))
help(factorial)
