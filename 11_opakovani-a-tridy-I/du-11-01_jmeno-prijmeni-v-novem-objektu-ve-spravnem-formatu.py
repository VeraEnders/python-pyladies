'''
Ukol 1
Zařiď, aby se při vytváření objektu zajistilo, že jméno i příjmení budou ve správném formátu, tzn. první písmeno velké, ostatní malá (např. Anna Nováková - správně, aNNa NoVáKoVá - špatně).

Otestujte (například) pomocí:
osoba = Clovek('anna', 'nová')
print(osoba.jmeno, osoba.prijmeni) # Anna Nová
osoba = Clovek('AnnA', 'nOVá')
print(osoba.jmeno, osoba.prijmeni) # Anna Nová
'''
class Clovek:
  def __init__(self, jmeno, prijmeni):
    self.jmeno = jmeno.capitalize()
    self.prijmeni = prijmeni.capitalize()

osoba = Clovek('anna', 'nová')
print(osoba.jmeno, osoba.prijmeni) # Anna Nová
osoba = Clovek('AnnA', 'nOVá')
print(osoba.jmeno, osoba.prijmeni) # Anna Nová