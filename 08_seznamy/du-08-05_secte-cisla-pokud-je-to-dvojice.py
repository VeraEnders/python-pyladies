'''
Ukol 5
Napiš funkci, která dostane dvojici (tzv. tuple) a vrátí její součet. 
Pokud funkce dostane více jak dvě čísla, tj. např. trojici, tak vypíše: "Bohužel, umím sečíst jen dvě čísla."
'''

def soucet_dvojice(tuple):
  if len(tuple) != 2:
    return 'Bohužel, umím sečíst jen dvě čísla.'
  else:
    return tuple[0] + tuple[1]
  
print(soucet_dvojice((1, 5)))
print(soucet_dvojice((5, 2, 7)))