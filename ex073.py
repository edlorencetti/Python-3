times = ('corinthians', 'palmeiras', 'santos', 'gremio', 'cruzeiro',
         'flamengo', 'vasco', 'chapecoense', ' atletico', 'botafogo',
         'atletico-pr', 'bahia', 'sao paulo', 'fluminense', 'sport recife',
         'ec vitoria', 'coritiba', 'avai', 'ponte preta', 'atletico-go')
print('-=' * 15)
print(f'lista de times: {times}')
print('-=' * 15)
print(f'Os cinco primeiros times: {times[0:5]}')
print('-=' * 15)
print(f'Os qatro ultimos sao {times[-4:]}')
print('-=' * 15)
print(f'Os times em ordem alfabetica: {sorted(times)}')
print('-=' * 15)
print(f'O chapecoense esta na {times.index("chapecoense")+1} posicao')# no caso de usar aspas dentro de aspas usar aspas duplas
print('-=' * 15)
