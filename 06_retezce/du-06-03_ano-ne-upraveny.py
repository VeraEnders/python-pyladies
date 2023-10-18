'''
Ukol 3
Změň funkci ano_nebo_ne z materiálů k lekci Vlastní funkce (sekce Vracení) tak, aby se místo ano se dalo použít i a, místo ne i n a aby se nebral ohled na velikost písmen a mezery před/za odpovědí.

Textům jako možná nebo no tak určitě by počítač dál neměl rozumět.
'''

def ano_nebo_ne(otazka):
  "Vrátí True nebo False, podle odpovědi uživatele"
  while True:
    odpoved = input(otazka)
    odpoved_upravena = odpoved.lower().strip()

    if odpoved_upravena == 'ano' or odpoved_upravena == 'a':
      return True
    elif odpoved_upravena == 'ne' or odpoved_upravena == 'n':
      return False
    else:
      print('Nerozumím! Odpověz "ano" nebo "ne".')

if ano_nebo_ne('Chceš si zahrát hru? '):
  print('OK! Ale napřed si ji musíš naprogramovat.')
else:
  print('Škoda.')