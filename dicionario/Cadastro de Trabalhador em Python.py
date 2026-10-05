from datetime import datetime
dados = dict()
dados['nome'] = str(input("Nome: "))
nasc = int(input("Ano de Nascimento: "))
dados['Idade'] = datetime.now().year - nasc
dados['Ctps'] = int(input("Carteira de Trabalho (0 não tem): "))
if dados['Ctps'] != 0:
    dados['contratação'] = int(input("Ano de Contratação: "))
    dados['Salario'] = float(input("Salario:  R$"))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print("-="*30)
for k, v in dados.items():
    print(f" - {k} tem o valor {v} ")
