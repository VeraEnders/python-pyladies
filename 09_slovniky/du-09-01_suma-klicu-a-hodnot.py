'''
Ukol 1
Napiš funkci, která sečte a vrátí sumu všech klíčů a sumu všech hodnot ve slovníku, který dostane jako argument. K vyzkoušení můžeš použít slovník z minulé úlohy. Například:

>>> soucet_klicu_a_hodnot(mocniny(4))
(10, 30)
>>> muj_slovnik = {0: 0, 1: 5, 2: 10}
>>> soucet_klicu_a_hodnot(muj_slovnik)
(3, 15)
'''
def soucet_klicu_a_hodnot(slovnik):
  # soucet_klicu = 0
  # soucet_hodnot = 0

  # for klic, hodnota in slovnik.items():
  #   soucet_klicu += klic
  #   soucet_hodnot += hodnota

  soucet_klicu = sum(slovnik.keys())
  soucet_hodnot = sum(slovnik.values())
  return (soucet_klicu, soucet_hodnot)

def mocniny(cislo):
  vysledek = {}
  for i in range(1, cislo + 1):
    vysledek[i] = i ** 2
  return vysledek

print(soucet_klicu_a_hodnot(mocniny(4)))

muj_slovnik = {0: 0, 1: 5, 2: 10}
print(soucet_klicu_a_hodnot(muj_slovnik))