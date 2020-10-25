f = input('Digite um frase: ').upper().strip()

print(f'A letra A aparece {f.count("A")} vezes na frase')
print(f'A letra A aparece a primeira vez na posição {f.find("A")+1 }')
print(f'A letra A aparece a utima vez na posição {f.rfind("A")+1}')
