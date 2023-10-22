# Úkol 4
# Napiš program, který po zadání správného hesla vypíše nějakou tajnou informaci.

tajemstvi = 'V pátek jsem viděla černého havrana.'
spravne_heslo = 'chcivedet'
heslo_input = input('Zadejte heslo: ')

if heslo_input == spravne_heslo:
  print(tajemstvi)
else:
  print('Špatné heslo')