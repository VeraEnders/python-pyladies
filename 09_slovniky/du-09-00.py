'''
Ukol 0
Napiš funkci, která pro argumentem zadané číslo n vytvoří a vrátí slovník, kde jako klíče budou čísla od jedné do n a jako hodnoty k nim jejich druhé mocniny. Například:

>>> mocniny(4)
{1: 1, 2: 4, 3: 9, 4: 16}
>>> mocniny(2)
{1: 1, 2: 4}
'''

def mocniny(cislo):
    vysledek = {}
    for i in range(1, cislo + 1):
        vysledek[i] = i ** 2
    return vysledek

print(mocniny(2))
print(mocniny(4))