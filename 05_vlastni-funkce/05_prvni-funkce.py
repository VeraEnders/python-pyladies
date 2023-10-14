# Vrátí obvod obdélníka daných rozměrů

def obvod_obdelnika(sirka, vyska):
  "Vrátí obvod obdélníka daných rozměrů"  # Tělo může začít dokumentačním řetězcem, který popisuje, co funkce dělá
  return 2 * (sirka + vyska)

print(obvod_obdelnika(4, 2))

# Když funkce neskončí příkazem return, automaticky se vrátí hodnota None.
def nic():
    "Tahle funkce nic nedělá"

print(nic()) # None