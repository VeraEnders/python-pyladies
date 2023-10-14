'''
Ukol 3
Pomocí cyklů for a parametru end pro print napiš program, který postupně z jednotlivých 'X' vypíše:
X X X X X
X X X X X
X X X X X
X X X X X
X X X X X
„Z jednotlivých 'X'“ znamená, že nepoužiješ např. print('X X X X X'), ani násobení řetězců, t. j. např. 5 * "X".

Jak pojmenuješ proměnnou cyklu? A tu druhou? Slovně zdůvodni.
'''

for radek in range(5):
  for pozice in range(5):
    print('X', end=' ')
  print()

# Proměnná 'radek' reprezentuje číslo řádku.
# Proměnná 'pozice' reprezentuje aktuální pozici na řádku.