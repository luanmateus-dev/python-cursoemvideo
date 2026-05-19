total=totcusto=cont=menor=0
barato=''
while True:
    produto= str(input("nome do produto: ")).strip().lower()
    preco= float(input("preço: R$"))
    cont+=1
    continuar=' '
    while continuar not in 'sn':
        continuar= str(input("quer continuar? [S/N] ")).strip().lower()[0]
    total+=preco
    if preco>1000:
        totcusto+=1
    if cont==1 or preco<menor:
        menor=preco
        barato=produto
    if continuar=='n':
        break
print(f"o total da compra foi de R${total:.2f}")
print(f"temos {totcusto} produtos custando mais de R$1000")
print(f"o produto mais barato foi a {barato} que custa R${menor:.2f}")