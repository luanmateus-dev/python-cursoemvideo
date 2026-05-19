listanum= list()
while True:
    n=int(input('digite um valor: '))
    if n not in listanum:
        listanum.append(n)
        print('adicionado com sucesso... ')
    else:
        print('numero digitado duplicado!! Nâo irei adicionar. ')
    continuar= str(input('quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == "N":
        break
print('='*30)
listanum.sort()
print(f'você digitou os valores {listanum} ')

