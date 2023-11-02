'''
Ukol 3
Napiš program, který seřadí seznam domácích zvířat podle abecedy. Víš, jaký je rozdíl mezi metodou sort a funkcí sorted?
'''
# Metoda sort() upravuje seznam na místě, nevrací nový seznam.
# Funkce sorted() nemění vstup, vrací nový seřazený seznam.

def serad_zvirata(seznam):
  vysledek = sorted(seznam)
  return vysledek

domaci_zvirata = ['pes', 'kočka', 'křeček', 'králík', 'želva', 'činčila', 'had']
print(serad_zvirata(domaci_zvirata))