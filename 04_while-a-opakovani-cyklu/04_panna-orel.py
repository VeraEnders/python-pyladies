import random

uspech = 0

while True:
  tah = random.randrange(2)
  if tah == 0:
    tah = 'panna'
  else:
    tah = 'orel'

  tip = input('Panna nebo orel nebo konec? ')

  if tip == tah:
    print('Trefa!')
    uspech += 1
    if uspech == 3:
      break
  elif tip == 'konec':
    break
  else:
    print('Těsně vedle :(')

print("Dosáhla jsi", uspech, "úspěchů")