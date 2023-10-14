# program který hází dokud nepadne 6
# vypisuje jednotlivé hody
# na závěr vypíše kolik bylo třeba pokusů

# Bonus: na závěr vypsat součet všech hodů

import random

pocet_hodu = 0
soucet_hodu = 0

while True:
  hod = random.randrange(1, 7)
  pocet_hodu += 1
  soucet_hodu += hod
  print('Vypadla', hod)
  if hod == 6:
    break

print('Bylo potřeba', pocet_hodu, 'hodů')
print('Součet hodů je', soucet_hodu)