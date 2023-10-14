'''
Ukol 4
Napiš program, který simuluje tuto hru:

První hráč hází kostkou (t.j. vybírají se náhodná čísla od 1 do 6), dokud nepadne šestka. Potom hází další hráč, dokud nepadne šestka i jemu. Potom hází hráč třetí a nakonec čtvrtý. Vyhrává ten, kdo na hození šestky potřeboval nejvíc hodů. (V případě shody vyhraje ten, kdo házel dřív.)
Program by měl vypisovat všechny hody a nakonec napsat, kdo vyhrál.
Poznámka: pokud nemáš předchozí úkol, tento také přeskoč.
'''

import random

pocet_hracu = 4
nejvetsi_soucet = 0
vyherce = 0

for hrac in range(1, pocet_hracu + 1):
  pocet_hodu = 0
  soucet_hodu = 0

  while True:
    hod = random.randrange(1, 7)
    pocet_hodu += 1
    soucet_hodu += hod
    print('Hráč', hrac,'hodil', hod)

    if hod == 6:
      break
  
  if soucet_hodu > nejvetsi_soucet:
    nejvetsi_soucet = soucet_hodu
    vyherce = hrac

  print('Hráč', hrac, 'potřeboval', pocet_hodu, 'hodů.', 'Součet hodů je', soucet_hodu)

print('Vyhrál hráč', vyherce, 'se součtem hodů', nejvetsi_soucet)

