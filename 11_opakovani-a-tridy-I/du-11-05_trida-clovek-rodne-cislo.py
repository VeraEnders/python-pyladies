'''
Ukol 5
Rozšiř třídu Clovek tak, aby při vytváření vedle jména a příjmení zpracovala rodné číslo. Třída si do atributů uloží rok, měsíc a den narození a pohlaví. Následně rozšiř metodu kdo_jsi o nové informace.
Pozn.: Lze použít funkci na zpracování rodného čísla z předchozí úlohy :)
Do řešení prosím nedávejte vlastní rodná čísla, ale pouze vymyšlená.

Otestujte (například) pomocí:
osoba = Clovek('anna', 'nová', '9057121234')
print(osoba.kdo_jsi()) # Jmenuji se Anna Nová, mé iniciály jsou AN, jsem žena rok narození 1990 a narozeniny mám 12.7.
osoba = Clovek('jan', 'malý', '0007021234')
print(osoba.kdo_jsi()) # Jmenuji se Jan Malý, mé iniciály jsou JM, jsem muž rok narození 2000 a narozeniny mám 2.7.
'''
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

  return (rok, mesic, den, pohlavi)

class Clovek:
  def __init__(self, jmeno, prijmeni, rodne_cislo):
    self.jmeno = jmeno.capitalize()
    self.prijmeni = prijmeni.capitalize()
    self.inicialy = self.jmeno[0] + self.prijmeni[0]
    self.rok, self.mesic, self.den, self.pohlavi = zpracuj_rodne_cislo(rodne_cislo)

  def kdo_jsi(self):
    return f'Jmenuji se {self.jmeno} {self.prijmeni}, mé iniciály jsou {self.inicialy}, jsem {self.pohlavi} rok narození {self.rok} a narozeniny mám {self.den}.{self.mesic}.'

osoba = Clovek('anna', 'nová', '9057121234')
print(osoba.kdo_jsi()) # Jmenuji se Anna Nová, mé iniciály jsou AN, jsem žena rok narození 1990 a narozeniny mám 12.7.
osoba = Clovek('jan', 'malý', '0007021234')
print(osoba.kdo_jsi()) # Jmenuji se Jan Malý, mé iniciály jsou JM, jsem muž rok narození 2000 a narozeniny mám 2.7.