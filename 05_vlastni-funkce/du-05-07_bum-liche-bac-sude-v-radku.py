'''
Ukol 7
Napiš funkci, která bude mít jako parametr jedno číslo (n) a vypíše n řádek. Na prvním řádku bude "Bum", na druhém "Bác", na třetím "Bum", atd. Využij funkci z předchozího úkolu.
Např.
>>> vypis_bum_bac(5) 
Bum
Bác
Bum
Bác
Bum
'''

def bum_nebo_bac(cislo):
  if cislo % 2 != 0:
    return 'Bum'
  else:
    return 'Bác'

def vypis_bum_bac(pocet_radku):
  for radek in range(1, pocet_radku + 1):
    print(bum_nebo_bac(radek))
  
vypis_bum_bac(5)