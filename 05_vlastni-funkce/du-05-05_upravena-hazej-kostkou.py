'''
Ukol 5

Vrať se k úkolu č. 4 z minulé lekce a zkus zpřehlednit kód použitím funkce. Funkce hazej_kostkou bude vracet počet pokusů než hráči padla šestka.

Ukol 4 (z minule lekce)
Napiš program, který simuluje tuto hru:
První hráč hází kostkou (t.j. vybírají se náhodná čísla od 1 do 6), dokud nepadne šestka. Potom hází další hráč, dokud nepadne šestka i jemu. Potom hází hráč třetí a nakonec čtvrtý. Vyhrává ten, kdo na hození šestky potřeboval nejvíc hodů. (V případě shody vyhraje ten, kdo házel dřív.)
Program by měl vypisovat všechny hody a nakonec napsat, kdo vyhrál.
'''

import random

def hazej_kostkou():
  pocet_hodu = 0

  while True:
    hod = random.randrange(1, 7)
    pocet_hodu += 1
    print('Hráč', hrac,'hodil', hod)

    if hod == 6:
      break

  return pocet_hodu

pocet_hracu = 4
max_pocet_hodu = 0
vyherce = 0

for hrac in range(1, pocet_hracu + 1):
  pocet_hodu_hrace = hazej_kostkou()

  if pocet_hodu_hrace > max_pocet_hodu:
    max_pocet_hodu = pocet_hodu_hrace
    vyherce = hrac

  print('Hráč', hrac, 'potřeboval', pocet_hodu_hrace, 'hodů.')

print('Vyhrál hráč', vyherce, 's počtem hodů', max_pocet_hodu)
