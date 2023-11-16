'''
Ukol 0
Napiš funkci, do které se vloží dvě čísla a ona vrátí jejich podíl. Pokud dojde na dělení nulou, tak vyhodí výjimku "Nulou dělit nelze!".
'''

def deleni():
  while True:
    try:
      a = int(input('Zadejte cele cislo a: '))
      b = int(input('Zadejte cele cislo b: '))

      return a / b
    
    except ValueError:
      print('Musíte zadat číslo! Zkuste znovu.')
    except ZeroDivisionError:
      print('Nulou dělit nelze!')

print(deleni())