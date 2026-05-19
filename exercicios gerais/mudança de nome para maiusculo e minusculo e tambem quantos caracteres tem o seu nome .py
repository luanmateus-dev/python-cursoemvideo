nome= str(input("qual seu nome completo")).strip()
maiu= nome.upper()
print("seu nome em letra maiuscula é: ",maiu)
minu= nome.lower()
print("seu nome em letra minusculo é: ",minu)
carac= len(nome)-nome.count(' ')
print(carac)
print(" seu primeiro nome tem {} letras".format(nome.find(" ")))


