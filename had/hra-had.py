def nakresli_mapu(seznam_souradnic, rozmer):
  "Nakreslí mřížku zadaného rozměru, na příslušná políčka doplní X, jinde tečku"

  mapa = []

  for _ in range(rozmer):
    mapa.append(['.'] * rozmer)

  for radek, pozice in seznam_souradnic:
    mapa[pozice][radek] = 'X'

  for i in mapa:
    print(' '.join(i))

def pohyb(seznam_souradnic, svetova_strana, rozmer):
  "Přidá k seznamu souřadnic poslední bod posunutý v určitém směru a smaže první bod"

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

  if novy_bod in seznam_souradnic[:-1]:
    raise ValueError('Game over.')

  if novy_bod[0] < 0 or novy_bod[1] < 0 or novy_bod[0] > (rozmer-1) or novy_bod[1] > (rozmer-1):
    raise ValueError('Game over.')
  
  seznam_souradnic.append(novy_bod)
  del seznam_souradnic[0]

souradnice = [(0, 0), (1, 0), (2, 0)]
rozmer_mapy = 10

while True:
  svetova_strana = input('Zadejte světovou stranu (s / j / z / v) nebo konec: ')

  if svetova_strana == 'konec':
    break

  if svetova_strana not in ['s', 'j', 'z', 'v']:
    print('Špatný vstup. Zkuste znovu.')
    continue
  
  pohyb(souradnice, svetova_strana, rozmer_mapy)
  nakresli_mapu(souradnice, rozmer_mapy)