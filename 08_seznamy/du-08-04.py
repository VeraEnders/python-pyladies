'''
Ukol 4
Napiš funkci, která dostane dva seznamy jmen zvířat a vrátí tři seznamy:

    zvířata, která jsou v obou seznamech současně (průnik množin: první ∩ druhá),
    zvířata, která jsou jen v prvním seznamu (rozdíl množin: první - druhá),
    zvířata, která jsou jen ve druhém seznamu (rozdíl množin: druhá - první).
'''
def prunik_a_rozdil(seznam1, seznam2):
  # průnik množin: první ∩ druhá
  prunik = []  
  for zaznam in seznam1:
    if zaznam in seznam2:
      prunik.append(zaznam)

  # rozdíl množin: první - druhá
  rozdil_1 = []
  for zaznam in seznam1:
    if zaznam not in seznam2:
      rozdil_1.append(zaznam)

  # rozdíl množin: druhá - první
  rozdil_2 = []
  for zaznam in seznam2:
    if zaznam not in seznam1:
      rozdil_2.append(zaznam)

  return prunik, rozdil_1, rozdil_2

zvirata_1 = ['pes', 'kočka', 'králík', 'činčila', 'had']
zvirata_2 = ['pes', 'želva', 'činčila']

prunik, rozdil_1, rozdil_2 = prunik_a_rozdil(zvirata_1, zvirata_2)

print('Zvířata v obou seznamech současně: ', prunik)
print('Zvířata jen v prvním seznamu: ', rozdil_1)
print('Zvířata jen ve druhém seznamu: ', rozdil_2)