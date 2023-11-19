import random

def nakresli_mapu(seznam_souradnic, seznam_ovoce, rozmer):
  mapa = []

  for _ in range(rozmer):
    mapa.append(['.'] * rozmer)

  for radek, pozice in seznam_souradnic:
    mapa[pozice][radek] = 'X'

  for radek, pozice in seznam_ovoce:
    mapa[pozice][radek] = '?'

  for i in mapa:
    print(' '.join(i))

def pohyb(seznam_souradnic, seznam_ovoce, svetova_strana, rozmer):
  posledni_bod = seznam_souradnic[-1]
  x = posledni_bod[0]
  y = posledni_bod[1]

  if svetova_strana == 's':
    y -= 1
  elif svetova_strana == 'j':
    y += 1
  elif svetova_strana == 'v':
    x += 1
  elif svetova_strana == 'z':
    x -= 1
  
  novy_bod = (x, y)

  if novy_bod in seznam_souradnic:
    raise ValueError('Game over.')

  if novy_bod[0] < 0 or novy_bod[1] < 0 or novy_bod[0] > (rozmer-1) or novy_bod[1] > (rozmer-1):
    raise ValueError('Game over.')
  
  seznam_souradnic.append(novy_bod)
  
  if novy_bod in seznam_ovoce:
    seznam_ovoce.remove(novy_bod)
    if not seznam_ovoce:
      pridej_ovoce(seznam_souradnic, seznam_ovoce, rozmer)
  else:
    del seznam_souradnic[0]

def pridej_ovoce(seznam_souradnic, seznam_ovoce, rozmer):
  while True:
    x = random.randrange(rozmer)
    y = random.randrange(rozmer)
    nove_ovoce = (x, y)
    if nove_ovoce not in seznam_ovoce and nove_ovoce not in seznam_souradnic:
      seznam_ovoce.append(nove_ovoce)
      break

souradnice = [(0, 0), (1, 0), (2, 0)]
rozmer_mapy = 10
ovoce = []
tah = 0

while True:
  svetova_strana = input('Zadejte světovou stranu (s / j / z / v) nebo konec: ')

  if svetova_strana == 'konec':
    break

  if svetova_strana not in ['s', 'j', 'z', 'v']:
    print('Špatný vstup. Zkuste znovu.')
    continue

  if tah % 30 == 0:
    pridej_ovoce(souradnice, ovoce, rozmer_mapy)
  
  pohyb(souradnice, ovoce, svetova_strana, rozmer_mapy)
  nakresli_mapu(souradnice, ovoce, rozmer_mapy)

  tah += 1