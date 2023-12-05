'''
Ukol 6 [Bonus] 
Rozšiř zpracování rodného čísla o jeho validaci. Pokud rodné číslo není validní, vyhoď výjimku.

U rodného čísla lze kontrolovat:
číslo má 10 znaků
číslo je beze zbytku dělitelné 11
měsíc je v rozsahu 1-12 nebo 51-62
(zjednodušeně) den je v rozsahu 1-31
cokoliv dalšího, co tě napadne
'''

def je_validni(rodne_cislo, mesic, den):
  if len(rodne_cislo) != 10: return
  
  if int(rodne_cislo) % 11 != 0: return

  if (1 < mesic > 12) or (51 < mesic > 62): return

  if (1 < den > 31): return

  return True

def zpracuj_rodne_cislo(rodne_cislo):
  rok = int(rodne_cislo[:2])
  if rok >= 54:
    rok += 1900
  else:
    rok += 2000
    
  mesic = int(rodne_cislo[2:4])

  if mesic > 12:
    pohlavi = 'žena'
    mesic -= 50
  else:
    pohlavi = 'muž'

  den = int(rodne_cislo[4:6])

  if not je_validni(rodne_cislo, mesic, den):
    raise ValueError('Rodné číslo není validní.')

  return (rok, mesic, den, pohlavi)

print(zpracuj_rodne_cislo('0007021234')) # (2000, 7, 2, 'muž')
print(zpracuj_rodne_cislo('7360285163')) # (1973, 10, 28, 'žena')
# print(zpracuj_rodne_cislo('0007021234456')) # ValueError: Rodné číslo není validní.
# print(zpracuj_rodne_cislo('234456')) # ValueError: Rodné číslo není validní.
# print(zpracuj_rodne_cislo('9037121234')) # ValueError: Rodné číslo není validní.
# print(zpracuj_rodne_cislo('9063121234')) # ValueError: Rodné číslo není validní.
# print(zpracuj_rodne_cislo('0007321234')) # ValueError: Rodné číslo není validní.