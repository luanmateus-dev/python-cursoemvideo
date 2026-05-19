sexo = str(input('digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('dados inválidos! confirme seu sexo: ')).strip().upper()[0]
print('sexo {} registrado com sucesso'.format(sexo))