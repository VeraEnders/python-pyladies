# vytvořit třídu pro kočku.

# Kočka umí mňoukat metodou zamnoukej.
# Kočka má na začátku (při vytvoření) 9 životů (nemůže mít nikdy víc než 9 nebo míň než 0!).
# Kočka umí říct, jestli je živá (nemá 0 životů), metodou je_ziva.
# Kočka může ztratit život metodou uber_zivot.
# Kočku můžeš nakrmit metodou snez, která bere 1 argument - nějaké konkrétní jídlo (řetězec). Pokud je toto jídlo "ryba", kočce se obnoví jeden život (pokud teda už není mrtvá, nebo nemá maximální počet životů).

class Kocka:
  def __init__(self, jmeno):
    self.jmeno = jmeno
    self.pocet_zivotu = 9

  def zamnoukej(self):
    print("Mnau, mnau, mnauuu!")
  
  def je_ziva(self):
    return self.pocet_zivotu > 0

  def uber_zivot(self):
    if not self.je_ziva():
      print("Nemuzes zabit uz mrtvou kocku!")
    else:
      self.pocet_zivotu -= 1
  
  def snez(self, jidlo):
    if not self.je_ziva():
      print("Je zbytecne krmit mrtvou kocku!")
      return
    if jidlo == "ryba" and self.pocet_zivotu < 9:
      self.pocet_zivotu += 1
      print("Kocka spapala rybu a obnovil se ji jeden zivot.")
    else:
      print("Kocka se krmi.")

micka = Kocka('Micka')
print(micka.jmeno)
print(micka.pocet_zivotu)

micka.zamnoukej()
micka.je_ziva()
micka.uber_zivot()
micka.je_ziva()

micka.snez('ryba')
micka.snez('ryba')
