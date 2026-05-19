times= ('palmeiras', 'flamengo', 'fluminense', 'são paulo', 'athletico-PR', 'bahia',
        'bragantino', 'coritiba', 'vitoria', 'botafogo', 'atletico-MG',
        'internacional', 'vasco da gama', 'gremio', 'cruzeiro', 'santos',
        'corinthias', 'mirassol', 'remo', 'chapecoense')
print('-='*140)
print(f"lista de times {times}")
print('-='*140)
print(f'os 5 primeiros colocados: {times[0:5]}')
print('-='*140)
print(f'os 4 ultimos colocados: {times[-4:]}')
print('-='*140)
print(f'tabela de times em ordem alfabetica: {sorted(times)}')
print('-='*140)
print(f'o time da chapecoense esta {times.index("chapecoense")+1}ª posição')