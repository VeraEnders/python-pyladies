'''
Ukol 2
Napiš funkci, která dostane jako argument seznam domácích zvířat a vrátí seznam těch, která začínají na k.
'''

def zacina_na_k(seznam):
  vysledek = []
  for slovo in seznam:
    if slovo.lower().startswith('k'):
      vysledek.append(slovo)
  return vysledek

domaci_zvirata = ['pes', 'kočka', 'křeček', 'králík', 'želva', 'činčila', 'had']
print(zacina_na_k(domaci_zvirata))