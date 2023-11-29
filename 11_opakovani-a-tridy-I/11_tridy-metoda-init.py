class Kotatko:
  # Metoda __init__ se zavolá automaticky, když se vytvoří nový objekt
  def __init__(self, jmeno):
    self.jmeno = jmeno

  # __str__ se volá, když je potřeba převést objekt na řetězec
  def __str__(self):
    return '<Kotatko jmenem {}>'.format(self.jmeno)

  def zamnoukej(self):
    print("{}: Mňau!".format(self.jmeno))

  def snez(self, jidlo):
    print("{}: Mňau mňau! {} mi chutná!".format(self.jmeno, jidlo))

mourek = Kotatko('Mourek')
mourek.zamnoukej()
