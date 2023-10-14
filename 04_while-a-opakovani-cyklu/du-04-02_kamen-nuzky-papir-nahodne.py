'''
Ukol 2
Změň program Kámen, nůžky, papír tak, aby se tah počítače určoval náhodně.

Nápověda: můžeš použít funkci randrange a nastavit tah_pocitace na:
'kámen', pokud je náhodné číslo 0,
'nůžky', pokud je náhodné číslo 1,
jinak na 'papír'.
'''
import random

while True:
  tah_pocitace = random.randrange(3)
  if tah_pocitace == 0:
    tah_pocitace = 'kámen'
  elif tah_pocitace == 1:
    tah_pocitace = 'nůžky'
  else:
    tah_pocitace = 'papír'

  tah_cloveka = input('kámen, nůžky, papír nebo konec? ')

  if tah_cloveka == 'konec':
    break

  if tah_cloveka == 'kámen' or tah_cloveka == 'nůžky' or tah_cloveka == 'papír':
    print('Tvoje volba:', tah_cloveka)
    print('Volba počítače:', tah_pocitace)

    if tah_pocitace == tah_cloveka:
      print('Plichta.')
    elif (tah_pocitace == 'kámen' and tah_cloveka == 'nůžky') or (tah_pocitace == 'nůžky' and tah_cloveka == 'papír') or (tah_pocitace == 'papír' and tah_cloveka == 'kámen'):
      print('Počítač vyhrál.')
    else:
      print('Vyhrála jsi!')
  else:
    print('Špatný vstup. Zadej kámen, nůžky, papír nebo konec.')
  print()