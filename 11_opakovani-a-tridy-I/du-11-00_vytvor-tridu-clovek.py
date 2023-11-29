'''
Ukol 0
Vytvoř třídu Clovek. Clovek má atributy jméno a příjmení, které se nastavují při vytváření objektu.

Otestujte (například) pomocí:
osoba = Clovek('Anna', 'Nová')
print(osoba.jmeno, osoba.prijmeni) # Anna Nová
'''

class Clovek:
  def __init__(self, jmeno, prijmeni):
    self.jmeno = jmeno
    self.prijmeni = prijmeni

osoba = Clovek('Anna', 'Nová')
print(osoba.jmeno, osoba.prijmeni) # Anna Nová