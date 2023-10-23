'''
Ukol 3
Napiš program, který se zeptá na 3 čísla a zjistí, jestli je jejich součet větší než 10. Dokážeš jej vymyslet tak, aby funkce input byla v kódu zapsaná jen jednou? ;)
'''
def je_soucet_vetsi():
  soucet = 0

  for i in range(3):
    while True:
      cislo = input('Zadejte číslo: ')
      if not cislo.isdigit():
        print('Špatný vstup. Nezadal/a jste číslo!')
      else:
        soucet += int(cislo)
        break
  
  return soucet > 10

print(f'Součet tří čísel je {"větší" if je_soucet_vetsi() else "menší"} než 10' )