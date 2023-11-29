class Kotatko:
  def zamnoukej(self):
    print("{}: Mňau!".format(self.jmeno))

  def snez(self, jidlo):
    print("{}: Mňau mňau! {} mi chutná!".format(self.jmeno, jidlo))

# Vytvoření konkrétního objektu (angl. instance) 
mourek = Kotatko()
mourek.jmeno = 'Mourek'

micka = Kotatko()
micka.jmeno = 'Micka'

print(mourek.jmeno)
print(micka.jmeno)

# Volání metody
mourek.zamnoukej()
micka.zamnoukej()

mourek.snez('ryba')