def area(largura,comprimento):
    area = largura * comprimento
    print(f'A AREA DE UM TERRENO {largura}x{comprimento} vale {area:.2f}m^2.')

largura = float(input("LARGURA(m): "))
comprimento = float(input("COMPRIMENTO(m): "))
area(largura, comprimento)


