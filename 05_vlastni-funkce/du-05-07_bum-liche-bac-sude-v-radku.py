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

def vypis_bum_bac(pocet_radku):
  for radek in range(1, pocet_radku + 1):
    if radek % 2 != 0:
      print('Bum')
    else:
      print('Bác')
  
vypis_bum_bac(5)