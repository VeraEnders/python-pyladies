'''
Ukol 0
Napiš funkci, do které se vloží dvě čísla a ona vrátí jejich podíl. Pokud dojde na dělení nulou, tak vyhodí výjimku "Nulou dělit nelze!".
'''

def deleni(a, b):
  if b == 0:
    raise ValueError('Nulou dělit nelze!')

  return a / b

print(deleni(10, 2))
print(deleni(1, 0))
