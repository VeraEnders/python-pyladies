'''
Ukol 3, 4, 5
Následující projekty závisí jeden na druhém, řeš je postupně. Až to uděláš, můžeš si zahrát hru!
Tahle sekce není jednoduchá. Můžeš zkusit spojit síly s ostatními účastnicemi kurzu!
'''
'''
Ukol 3
Napiš funkci, která dostane seznam souřadnic (párů čísel menších než 10, která určují sloupec a řádek) a vypíše je jako mapu: mřížku 10×10, kde na políčka, která jsou v seznamu, napíše X, jinde tečku. Například:

nakresli_mapu([(0, 0), (1, 0), (2, 2), (4, 3), (8, 9), (8, 9)])
X X . . . . . . . .
. . . . . . . . . .
. . X . . . . . . .
. . . . X . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . X .
Jak na to?

Udělej tabulku (seznam seznamů) se samými tečkami, něco jako:
[['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']].
Na příslušných místech nahraď tečky X-ky.
Tabulku vypiš pomocí dvou cyklů for zanořených do sebe.
'''

def nakresli_mapu(seznam_souradnic, rozmer):
  mapa = []

  for _ in range(rozmer):
    mapa.append(['.'] * rozmer)

  for radek, pozice in seznam_souradnic:
    mapa[pozice][radek] = 'X'

  for i in mapa:
    print(' '.join(i))

# nakresli_mapu([(0, 0), (1, 0), (2, 2), (4, 3), (8, 9), (8, 9)])

'''
Ukol 4
Napiš funkci pohyb, která dostane seznam souřadnic a světovou stranu ("s", "j", "v" nebo "z") a přidá k seznamu poslední bod „posunutý“ v daném směru. Např.:

souradnice = [(0, 0)]
pohyb(souradnice, 'v')
print(souradnice)         # → [(0, 0), (1, 0)]
pohyb(souradnice, 'v')
print(souradnice)         # → [(0, 0), (1, 0), (2, 0)]
pohyb(souradnice, 'j')
print(souradnice)         # → [(0, 0), (1, 0), (2, 0), (2, 1)]
pohyb(souradnice, 's')
print(souradnice)         # → [(0, 0), (1, 0), (2, 0), (2, 1), (2, 0)]
Funkce by neměla nic vracet. Jen mění už existující seznam.
'''

def pohyb(seznam_souradnic, svetova_strana, rozmer):
  posledni_bod = seznam_souradnic[-1]
  x = posledni_bod[0]
  y = posledni_bod[1]

  if svetova_strana == 's':
    seznam_souradnic.append((x, (y - 1) % rozmer))
  elif svetova_strana == 'j':
    seznam_souradnic.append((x, (y + 1) % rozmer))
  elif svetova_strana == 'v':
    seznam_souradnic.append(((x + 1) % rozmer, y))
  elif svetova_strana == 'z':
    seznam_souradnic.append(((x - 1) % rozmer, y))

# souradnice = [(0, 0)]
# pohyb(souradnice, 'v')
# print(souradnice)         # → [(0, 0), (1, 0)]
# pohyb(souradnice, 'v')
# print(souradnice)         # → [(0, 0), (1, 0), (2, 0)]
# pohyb(souradnice, 'j')
# print(souradnice)         # → [(0, 0), (1, 0), (2, 0), (2, 1)]
# pohyb(souradnice, 's')
# print(souradnice)         # → [(0, 0), (1, 0), (2, 0), (2, 1), (2, 0)]

'''
Ukol 5
Napiš cyklus, který se bude ptát uživatele na světovou stranu, podle ní zavolá pohyb, a následně vykreslí seznam jako mapu. Pak se opět se zeptá na stranu atd.

Začínej se seznamem [(0, 0), (1, 0), (2, 0)].
'''

souradnice = [(0, 0), (1, 0), (2, 0)]
rozmer_mapy = 10

while True:
  svetova_strana = input('Zadejte světovou stranu (s / j / z / v) nebo konec: ')

  if svetova_strana == 'konec':
    break

  if svetova_strana not in ['s', 'j', 'z', 'v']:
    print('Špatný vstup. Zkuste znovu.')
    continue
  
  pohyb(souradnice, svetova_strana, rozmer_mapy)
  nakresli_mapu(souradnice, rozmer_mapy)
