'''
Ukol 5
Napiš funkci, která dostane jako parametry tři čísla a zjistí, jestli je jejich součet větší než 10. Funkce by měla vracet vracet True nebo False.
'''

def je_soucet_vetsi(a, b, c):
  soucet = a + b + c
  return soucet > 10

print(je_soucet_vetsi(1, 9, 10))
print(je_soucet_vetsi(2, 2, 5))