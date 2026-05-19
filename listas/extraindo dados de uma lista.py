lista= list()
while True:
    lista.append(int(input('digite um valor: ')))
    continuar = str(input('quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
lista.sort(reverse=True)
print(f'você digitou {len(lista)} elementos. ')
print(f'os valores em ordem decrescente são {lista}. ')
if 5 in lista:
    print('o numero 5 faz parte da lista. ')
else:
    print('o numero 5 não foi encontrado! ')