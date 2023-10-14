# Globální proměnné 
# existují v celém programu
# ve funkcích, které mají náhodou lokální proměnnou stejného jména, „nejsou vidět“ – to jméno označuje lokální proměnnou

pi = 3.1415926 # globální proměnná

def obsah_kruhu(polomer):
  return pi * polomer ** 2

print(obsah_kruhu(100))


# Lokální proměnné 
# existují jen v rámci volání jedné jediné funkce

# Takže tohle nebude fungovat tak, jak se zdá:
x = 0

def nastav_x(hodnota):
  x = hodnota  # Přiřazení do lokální proměnné!

nastav_x(40)
print(x)

# Je lokální, nebo globální?
from math import pi
obsah = 0
a = 30

def obsah_elipsy(a, b):
    obsah = pi * a * b  # Přiřazení do `obsah`
    a = a + 3  # Přiřazení do `a`
    return obsah

print(obsah_elipsy(a, 20))
print(obsah)
print(a)

'''
Je proměnná pi lokální, nebo globální? - globální. Nepřiřazuje se do ní ve funkci; je „vidět“ v celém programu.
Je proměnná obsah lokální, nebo globální? - Proměnné obsah jsou v programu dvě – jedna globální, a jedna je lokální pro funkci obsah_elipsy, protože do ní tahle funkce přiřazuje.
Je proměnná a lokální, nebo globální? - Proměnné a jsou taky dvě, podobně jako obsah. Tady byl chyták: příkaz a = a + 3 nemá žádný smysl; do a se sice uloží větší číslo, ale vzápětí funkce obsah_elipsy skončí a její lokální proměnná a přestane existovat.
Je proměnná b lokální, nebo globální? - Proměnná b je jenom lokální – jako argument funkce obsah_elipsy.
'''