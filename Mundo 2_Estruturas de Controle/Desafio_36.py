vc = float(input('Digite o valor da casa: '))
sl = float(input('Digite o seu salário: '))
qa = float(input('Digite em quantos anos deseja pagar: '))

vpa = vc/qa
vpm = vpa/12
cc = 0.3*sl


if vpm > 0.3*sl:
    print(f'Empréstimo Negado! Você teria que pagar uma mensalidade de {vpm:.2f} R$. O correto seria {cc:.2f} R$ mensais.')
else:
    print(f'Empréstimo Aceito! Sua parcela mensal é de {vpm:.2f} R$')
