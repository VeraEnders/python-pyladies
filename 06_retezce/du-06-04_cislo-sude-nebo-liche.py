'''
Ukol 4
Napiš funkci, která dostane jako parametr číslo a zjistí, jestli je sudé. Funkce by měla vracet True nebo False.
'''

def je_cislo_sude(cislo):
  return cislo % 2 == 0

print(je_cislo_sude(15))
print(je_cislo_sude(4))