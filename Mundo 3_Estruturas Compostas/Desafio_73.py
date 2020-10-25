times = ('FLAMENGO', 'SANTOS', 'PALMEIRAS','GRÊMIO', 'ATHLETICO-PR',
         'SÃO PAULO', 'INTERNACIONAL','CORINTHIANS','FORTALEZA','GOIÁS','BAHIA',
         'VASCO','ATLÉTICO-MG','FLUMINENSE','BOTAFOGO','CEARÁ','CRUZEIRO','CSA',
         'CHAPECOENSE','AVAÍ')

print(f'\n{" CAMPEONATO BRASILEIRO 2019 ":-^40}\n')
for pos,t in enumerate(times):
    print(f'{t} -> {pos+1}º POSIÇÃO')
print('='*110)
print(f'\nCLASSIFICADOS PARA LIBERTADORES 2020 -> {times[:6]}')
print('='*110)
print(f'\nREBAIXADOS -> {times[16:]}')
print('='*110)
print(f'\nORGANIZADO EM ORDEM ALFABÉTICA -> {sorted(times)}')
print('='*110)
print(f'\nA CHAPE ESTÁ NA {times.index("CHAPECOENSE")+1}º POSIÇÂO.')
print('='*110)
