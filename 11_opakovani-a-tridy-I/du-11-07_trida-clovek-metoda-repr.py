'''
Ukol 7 [Bonus] 
Rozšiř třídu Clovek o metodu __repr__, která bude vracet stejný řetězec jako metoda kdo_jsi. Vyzkoušej funkci print na instanci objektu před a po přidání metody __repr__, vidíš nějaký rozdíl?

Otestujte (například) pomocí:
# před přidáním __repr__
osoba = Clovek('anna', 'nová', '9057121234')
print(osoba)

# přidej __repr__ a vyzkoušej znovu
osoba = Clovek('anna', 'nová', '9057121234')
print(osoba)
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

  def __repr__(self):
    # return self.kdo_jsi()
    return f'Jmenuji se {self.jmeno} {self.prijmeni}, mé iniciály jsou {self.inicialy}, jsem {self.pohlavi} rok narození {self.rok} a narozeniny mám {self.den}.{self.mesic}.'

  def kdo_jsi(self):
    return f'Jmenuji se {self.jmeno} {self.prijmeni}, mé iniciály jsou {self.inicialy}, jsem {self.pohlavi} rok narození {self.rok} a narozeniny mám {self.den}.{self.mesic}.'

# před přidáním __repr__
osoba = Clovek('anna', 'nová', '9057121234')
print(osoba) #-> <__main__.Clovek object at 0x000001CFB843FC90>

# přidej __repr__ a vyzkoušej znovu
osoba = Clovek('anna', 'nová', '9057121234')
print(osoba) #-> Jmenuji se Anna Nová, mé iniciály jsou AN, jsem žena rok narození 1990 a narozeniny mám 12.7.