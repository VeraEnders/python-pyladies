'''
Ukol 3
Rozšiř třídu Clovek tak, aby při vytváření třídy došlo k uložení iniciál do atributu inicialy a následně rozšiř metodu kdo_jsi, aby uvedla rovněž iniciály.

Otestujte (například) pomocí:

osoba = Clovek('anna', 'nová')
print(osoba.inicialy) # AN
print(osoba.kdo_jsi()) # Jmenuji se Anna Nová a mé iniciály jsou AN
'''
class Clovek:
  def __init__(self, jmeno, prijmeni):
    self.jmeno = jmeno.capitalize()
    self.prijmeni = prijmeni.capitalize()
    self.inicialy = self.jmeno[0] + self.prijmeni[0]

  def kdo_jsi(self):
    return f'Jmenuji se {self.jmeno} {self.prijmeni} a mé iniciály jsou {self.inicialy}'

osoba = Clovek('anna', 'nová')
print(osoba.inicialy) # AN
print(osoba.kdo_jsi()) # Jmenuji se Anna Nová a mé iniciály jsou AN