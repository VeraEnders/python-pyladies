# program který hází 3 kostkami dokud nepadne 6 na všech
# na závěr vypíše kolik bylo třeba pokusů

import random

pocet_pokusu = 0

while True:
  uspech = 0
  for kostka in range(3):
    hod = random.randrange(1, 7)
    if hod == 6:
        uspech += 1
  pocet_pokusu += 1
  print("pokus", pocet_pokusu, "uspechu", uspech)
  if uspech == 3:
        break

print('Bylo potřeba', pocet_pokusu, 'hodů')