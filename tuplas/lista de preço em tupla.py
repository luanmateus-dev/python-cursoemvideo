listagem= ('BORRACHA', 1,
           'CANETA',0.76,
           'CADERNO',27.99,
           'MOCHILA',49.99,
           'MARCA TEXTO',3)
print('-'*40)
print(f'{"LISTA DE PREÇO":^40}')
print('-'*40)
for pos in range(0,len(listagem)):
    if pos %2==0:
        print(f'{listagem[pos]:.<30}', end='' )
    else:
        print(f'R${listagem[pos]:>5.2f}')
print('-'*40)


