def ficha(jog='<esconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input("Nome do jogador: "))
g = str(input("Número de gol: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
