'''
Ukol 1
Změň program Kámen, nůžky, papír z úkolu 7 po druhé lekci tak, aby opakoval hru, dokud uživatel nezadá konec.
'''
# Zkus napsat hru Kámen, nůžky, papír. Jak na to:
# Vytvoř si dvě proměnné, tah_cloveka a tah_pocitace
# Nastav tah_pocitace na "kámen", na tah_cloveka se uživatele zeptej
# Vypiš výsledky hry dle tahu člověka - buď 'Plichta.', 'Počítač vyhrál.' nebo 'Vyhrála jsi!'. 
# Vyhodnocení výsledku hry naprogramuj tak, jako by počítač mohl náhodně losovat ze všech tří variant - naučíš ho to v příští lekci.

tah_pocitace = 'kámen'

while True:
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