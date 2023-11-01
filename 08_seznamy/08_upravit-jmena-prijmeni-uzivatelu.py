'''
Představ si, že ti uživatelé zadávají jména a příjmení a ty si je ukládáš do seznamu 
pro další použití např. v evidenci studentů. Ne všichni jsou ale pořádní, 
a tak se v seznamu sem tam objeví i jméno s nesprávně zadanými velkými písmeny. 
Například:
zaznamy = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník']

Úkolem je:
Napsat funkci, která vybere jen ty správně zadané záznamy, které mají správně 
jméno i příjmení s velkým počátečním písmenem.
Napsat funkci, která vybere naopak jen ty nesprávně zadané záznamy.
(Nepovinný) - Napsat funkci, která vrátí seznam s opravenými záznamy.
'''

zaznamy = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník']

def vyber_chybne(seznam):
  vysledek = []
  for zaznam in seznam:
    jmeno_a_prijmeni = zaznam.split(' ')
    jmeno = jmeno_a_prijmeni[0]
    prijmeni = jmeno_a_prijmeni[1]
    if jmeno[0].islower() or prijmeni[0].islower():
      vysledek.append(zaznam)
  return vysledek
  
def vyber_spravne(seznam):
  vysledek = []
  for zaznam in seznam:
    jmeno_a_prijmeni = zaznam.split(' ')
    jmeno = jmeno_a_prijmeni[0]
    prijmeni = jmeno_a_prijmeni[1]
    if not jmeno[0].islower() and not prijmeni[0].islower():
      vysledek.append(zaznam)
  return vysledek
  
def oprav_zaznamy(seznam):
  vysledek = []
  for zaznam in seznam:
    jmeno_a_prijmeni = zaznam.split(' ')
    jmeno = jmeno_a_prijmeni[0]
    prijmeni = jmeno_a_prijmeni[1]
    vysledek.append(jmeno.capitalize() + ' ' + prijmeni.capitalize())
  return vysledek

chybne_zaznamy = vyber_chybne(zaznamy)
print(chybne_zaznamy) # → ['pepa novák', 'Ivo navrátil', 'jan Poledník']

spravne_zaznamy = vyber_spravne(zaznamy)
print(spravne_zaznamy) # → ['Jiří Sládek']

opravene_zaznamy = oprav_zaznamy(zaznamy)
print(opravene_zaznamy) # → ['Pepa Novák', 'Jiří Sládek', 'Ivo Navrátil', 'Jan Poledník']