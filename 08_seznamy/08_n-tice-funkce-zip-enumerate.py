# Funkce `zip`
# Používá se ve for cyklech, podobně jako funkce range, která „dává” čísla.
# dostane n seznamů (či jiné věci použitelné ve for), „dává” n-tice

osoby = 'máma', 'teta', 'babička', 'vrah'
vlastnosti = 'hodná', 'milá', 'laskavá', 'zákeřný'
for osoba, vlastnost in zip(osoby, vlastnosti):
  print('{} je {}'.format(osoba, vlastnost))

# Funkce enumerate
# bere seznam a spáruje index (pořadí v seznamu) s příslušným prvkem
prvocisla = [2, 3, 5, 7, 11, 13]
for i, prvocislo in enumerate(prvocisla):
  print('Prvočíslo č.{} je {}'.format(i, prvocislo))