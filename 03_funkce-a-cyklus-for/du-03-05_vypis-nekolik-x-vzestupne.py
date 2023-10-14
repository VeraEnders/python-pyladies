'''
Ukol 5
Napiš program, který postupně z jednotlivých 'X' vypíše:
X
X X
X X X
X X X X

'''

for radek in range(1, 5):
  pocet_x = radek
  for pozice in range(pocet_x):
    print('X', end=' ')
  print()
