'''
Ukol 3
Napiš program, který se ptá uživatele na čísla do té doby, než zadá 0. Poté vypíše nejmenší ze zadaných čísel. (Pozor: nula se mezi porovnávaná čísla nepočítá.)
Nápověda: průběžně stačí ukládat jen údaj, které číslo je aktuálně to nejmenší.
'''

zadane_cislo = float(input('Zadej libovolné číslo (0 ukončí program): '))
nejmensi_cislo = zadane_cislo

if zadane_cislo != 0:
  while True:
    zadane_cislo = float(input('Zadej libovolné číslo (0 ukončí program): '))

    if zadane_cislo == 0:
      break
    
    if zadane_cislo < nejmensi_cislo:
      nejmensi_cislo = zadane_cislo
      
  print('Nejmenší zadané číslo je', nejmensi_cislo)
else:
  print('Nebyla zadána žádná čísla k porovnání.')