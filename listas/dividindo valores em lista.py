lista= list()
pares= list()
impares= list()
while True:
    lista.append(int(input('digite um valor: ')))
    continuar = str(input('quer continuar? [S/N] ')).strip()
    if continuar in 'Nn':
        break
print(f'A lista completa é {lista} ')
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
      impares.append(v)
print(f'A lista de pares é {pares} ')
print(f'A lista de impares é {impares} ')

