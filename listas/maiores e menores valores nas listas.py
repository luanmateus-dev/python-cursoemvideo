listanum= []
maior=menor=0
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor na poosição {c}: ')))
    if c==0:
        maior=menor=listanum[c]
    else:
        if listanum[c]>maior:
            maior=listanum[c]
        if listanum[c]<menor:
            menor=listanum[c]
print(f'Você digitou os valores {listanum} ')
print(f'o maior valor digitado foi {maior} na posição ',end='' )
for i,v in enumerate(listanum):
    if v==maior:
        print(f'{i}... ',end='')
print()
print(f'o menor valor digitado foi {menor} na posição ',end='' )
for i, v in enumerate(listanum):
    if v==menor:
        print(f'{i}... ',end='')
print()











