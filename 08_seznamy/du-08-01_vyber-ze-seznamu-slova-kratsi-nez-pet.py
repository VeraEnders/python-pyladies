'''
Ukol 1
Napiš funkci, která dostane jako argument seznam domácích zvířat a vrátí seznam těch, která jsou kratší než 5 písmen.
'''
def kratsi_nez_pet(seznam):
  vysledek = []
  for slovo in seznam:
    if len(slovo) < 5:
      vysledek.append(slovo)
  return vysledek

domaci_zvirata = ['pes', 'kočka', 'křeček', 'králík', 'želva', 'činčila', 'had']
print(kratsi_nez_pet(domaci_zvirata))