'''
Ukol 6
Napiš funkci, která bude mít jako parametr jedno číslo a vrátí "Bum", je-li toto číslo liché, a "Bác", je-li toto číslo sudé.
'''

def vypis_bum_bac(cislo):
  if cislo % 2 != 0:
    return 'Bum'
  else:
    return 'Bác'
  
print(vypis_bum_bac(5))
print(vypis_bum_bac(12))