'''
Ukol 6
Had byl pyšný na to, že je v abecedě první. Dokud nepřiletěla "andulka".
Abys hada uklidnila, vytvoř funkci, která zvířata seřadí podle abecedy, ale bude ignorovat první písmeno t.j. vrátí:
"had",
"pes",
"andulka",
"kočka",
"králík".

Postup:
    Máš seznam hodnot, které chceš seřadit podle nějakého klíče. Klíč se dá z každé hodnoty vypočítat.
    Vytvoř seznam dvojic (klíč, hodnota).
    Seřaď tento seznam dvojic – dvojice se řadí nejdřív podle prvního prvku, pak druhého atd.
    Nakonec vytvoř ze seznamu dvojic opět jen seznam hodnot.

Proč má zrovna had takovéhle výsadní postavení, zjistíš později.
'''
def seradit(seznam):
  seznam_dvojic = []
  for zaznam in seznam:
    seznam_dvojic.append((zaznam[1:], zaznam))
  
  serazene_dvojice = sorted(seznam_dvojic)

  vysledek = []
  for dvojice in serazene_dvojice:
    vysledek.append(dvojice[1])
  
  return vysledek

zvirata = ['králík', 'had', 'andulka', 'kočka', 'pes']
print(seradit(zvirata))