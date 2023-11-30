'''
Ukol 2
Přidej třídě Clovek metodu kdo_jsi, která danou osobu představí.

Otestujte (například) pomocí:
osoba = Clovek('anna', 'nová')
print(osoba.kdo_jsi()) # Jmenuji se Anna Nová
'''
class Clovek:
  def __init__(self, jmeno, prijmeni):
    self.jmeno = jmeno.capitalize()
    self.prijmeni = prijmeni.capitalize()

  def kdo_jsi(self):
    return f'Jmenuji se {self.jmeno} {self.prijmeni}'

osoba = Clovek('anna', 'nová')
print(osoba.kdo_jsi()) # Jmenuji se Anna Nová