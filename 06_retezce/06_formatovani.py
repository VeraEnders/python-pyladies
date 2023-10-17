def bum_nebo_bac(cislo):
  if cislo % 2 != 0:
    return 'Bum'
  else:
    return 'Bác'

def vypis_bum_bac(pocet_radku):
  for radek in range(1, pocet_radku + 1):
    slovo = bum_nebo_bac(radek)

    # print(radek, '-', bum_nebo_bac(radek))
    print(f'Radek #{radek:2d}: vysledek je {slovo}')
  
vypis_bum_bac(8)