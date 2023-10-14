# Zkus napsat funkci, která vrátí obsah elipsy daných rozměrů. 
# Příslušný vzoreček je A = πab, kde a a b jsou délky os.

import math

def obsah_elipsy(a, b):
  "Vrátí obsah elipsy s poloosami daných délek"
  return math.pi * a * b

x = float(input('Zadej délku poloosy 1: '))
y = float(input('Zadej délku poloosy 2: '))
print('Obsah elipsy je', obsah_elipsy(x, y))

# Funkci, která výsledek vrací, můžeš použít v dalších výpočtech:
def objem_eliptickeho_valce(a, b, vyska):
  return obsah_elipsy(a, b) * vyska

print('Obsah eliptického valce je', objem_eliptickeho_valce(x, y, 3))