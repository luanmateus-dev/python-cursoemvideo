n1= (int(input('digite um numero: ')),
     int(input('digite outro numero: ')),
     int(input('digite mais um numero: ')),
     int(input('digite o ultimo numero: ')))
print(f'os numeros digitados foram {n1}')
print(f'o numero 9 apareceu {n1.count(9)} vezes')
if 3 in n1:
    print(f'o numero 3 apareceu na {n1.index(3)+1}ª posição ')
else:
    print('o numero 3 não foi digitado')
print('os numeros pares digitados foram ', end='')
for n in n1:
    if n%2==0:
        print(n,end=' ')
