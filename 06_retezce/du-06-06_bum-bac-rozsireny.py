'''
Ukol 6
Napiš funkci, která vypíše čísla od jedné do 100, ale:

Pokud je číslo dělitelné třemi, napíše místo něj "bum".
Pokud je číslo dělitelné pěti, napíše místo něj "bác".
Pokud je číslo dělitelné pěti i třemi zároveň, napíše místo toho "bum-bác".
'''

def bum_bac():
  vysledek = ''

  for cislo in range(1, 101):
    if cislo % 3 == 0 and cislo % 5 == 0:
      vysledek += 'bum-bác'
    elif cislo % 3 == 0:
      vysledek += 'bum'
    elif cislo % 5 == 0:
      vysledek += 'bác'
    else:
      vysledek += str(cislo)
      
    vysledek += ' '

  return vysledek

print(bum_bac())