'''
Ukol 2
Napiš funkci, která jako argument dostane řetězec a vrátí slovník, ve kterém budou jako klíče jednotlivé znaky ze zadaného řetězce a jako hodnoty počty výskytů těchto znaků v řetězci. Například:

>>> pocet_znaku("hello world")
{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
Co vrátí funkce, když jejím argmentem bude "Máme rádi PyLadies!"?

Zkus se obejít bez použítí metody count.
'''
def pocet_znaku(retezec):
  slovnik = {}
  for pismeno in retezec:
    if slovnik.get(pismeno):
      slovnik[pismeno] += 1
    else:
      slovnik[pismeno] = 1

  return slovnik

print(pocet_znaku("hello world"))
print(pocet_znaku("Máme rádi PyLadies!"))