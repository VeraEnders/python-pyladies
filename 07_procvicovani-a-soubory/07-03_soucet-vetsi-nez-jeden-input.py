'''
Ukol 3
Napiš program, který se zeptá na 3 čísla a zjistí, jestli je jejich součet větší než 10. Dokážeš jej vymyslet tak, aby funkce input byla v kódu zapsaná jen jednou? ;)
'''
def je_soucet_vetsi():
  pocet_cisel = 3
  print(f'Zadejte postupně {pocet_cisel} čísel, pak vyhodnotím, jestli je jejich součet větší než 10.')

  soucet = 0

  for i in range(pocet_cisel):
    while True:
      cislo = input('Zadejte číslo: ')
      if not isinstance(cislo, int) or not isinstance(cislo, float):
        print('Špatný vstup. Nezadal/a jste číslo!')
      else:
        soucet += float(cislo)
        break
  
  return soucet

print(je_soucet_vetsi())