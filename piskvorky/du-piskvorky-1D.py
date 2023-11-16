# Hra piškvorky

# 1-D piškvorky se hrají na řádku s dvaceti políčky. Hráči střídavě přidávají kolečka ('o') a křížky ('x'), třeba:
# 1. kolo: -------x------------
# 2. kolo: -------x--o---------
# 3. kolo: -------xx-o---------
# 4. kolo: -------xxoo---------
# 5. kolo: ------xxxoo---------
# Hráč, který dá tři své symboly vedle sebe, vyhrál.

'''
Napiš funkci vyhodnot, která dostane řetězec s herním polem 1-D piškvorek a vrátí jednoznakový řetězec podle stavu hry:
"x" - Vyhrál hráč s křížky (pole obsahuje "xxx")
"o" - Vyhrál hráč s kolečky (pole obsahuje "ooo")
"!" - Remíza (pole neobsahuje "-", a nikdo nevyhrál)
"-" - Ani jedna ze situací výše (t.j. hra ještě neskončila)
'''
def vyhodnot(pole):  
  if 'xxx' in pole:
    return 'x'
  elif 'ooo' in pole:
    return 'o'
  elif '-' not in pole:
    return '!'
  else:
    return '-'

'''
Napiš funkci tah, která dostane řetězec s herním polem, číslo políčka (0-19), a symbol (x nebo o) a vrátí herní pole (t.j. řetězec) s daným symbolem umístěným na danou pozici.
'''
def tah(pole, cislo_policka, symbol):
  return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]

'''
Napiš funkci tah_hrace, která dostane řetězec s herním polem, zeptá se hráče, na kterou pozici chce hrát, a vrátí herní pole se zaznamenaným tahem hráče. Funkce by měla odmítnout záporná nebo příliš velká čísla a tahy na obsazená políčka. Pokud uživatel zadá špatný vstup, funkce mu vynadá a zeptá se znova.
'''
def tah_hrace(pole):
  while True:
    tah_input = input(f'Zadejte pozici od 0 do {len(pole) - 1}, kam chcete umístit symbol: ')

    if not tah_input.isdigit():
      print('\N{BALLOT X} Špatný vstup. Nezadal/a jste číslo!')
    else:
      tah_input_cislo = int(tah_input)

      if tah_input_cislo not in range(0, len(pole)):
        print(f'\N{BALLOT X} Číslo pozice musí být od 0 do {len(pole) - 1}.')

      elif pole[tah_input_cislo] != '-':
        print(f'\N{BALLOT X} Políčko je již obsazené.')

      else:
        pole_nove = tah(pole, tah_input_cislo, 'x')
        return pole_nove

'''
Napiš funkci tah_pocitace, která dostane řetězec s herním polem, vybere pozici, na kterou hrát, a vrátí herní pole se zaznamenaným tahem počítače.
Použij jednoduchou náhodnou „strategii”:
 - Vyber číslo od 0 do 19.
 - Pokud je dané políčko volné, hrej na něj.
 - Pokud ne, opakuj od bodu 1.
Můžeš předpokládat, že řetězec s herním polem vždy obsahuje alespoň jednu volnou pozici.
'''
# import random 
# def tah_pocitace(pole):
#   while True:
#     tah_nahodny = random.randrange(len(pole))

#     if pole[tah_nahodny] == '-':
#       pole_nove = tah(pole, tah_nahodny, 'o')
#       return pole_nove

'''
Zvládneš pro počítač naprogramovat lepší strategii? Třeba aby se snažil hrát vedle svých existujících symbolů nebo aby bránil protihráčovi?
'''
import random 

def tah_pocitace(pole):
  # Počítač se snaží umístit 'o' vedle svých existujících symbolů
  array_o = ['-oo', 'o-o', 'oo-']

  for i in range(len(array_o)):
    index = pole.find(array_o[i])
    if index != -1:
      pole_nove = tah(pole, index + i, 'o')
      return pole_nove
    
  # Počítač se snaží umístit 'o' vedle symbolů 'x' protihráče
  array_x = ['-xx', 'x-x', 'xx-']

  for i in range(len(array_x)):
    index = pole.find(array_x[i])
    if index != -1:
      pole_nove = tah(pole, index + i, 'o')
      return pole_nove

  # Náhodné umístění 'o'
  while True:
    tah_nahodny = random.randrange(len(pole))

    if pole[tah_nahodny] == '-':
      pole_nove = tah(pole, tah_nahodny, 'o')
      return pole_nove
    
'''
Napiš funkci piskvorky1d, která vytvoří řetězec s herním polem a střídavě volá funkce tah_hrace a tah_pocitace, dokud někdo nevyhraje nebo nedojde k remíze.
Nezapomeň kontrolovat stav hry po každém tahu.
'''
def piskvorky1d():
  pole = '-' * 20
  kolo = 0
  print(f'{kolo}. kolo: {pole}')

  while True:
    pole = tah_hrace(pole)
    kolo += 1
    print(f'{kolo}. kolo: {pole}')

    stav = vyhodnot(pole)
    if stav != '-':
      break

    pole = tah_pocitace(pole)
    kolo += 1
    print(f'{kolo}. kolo: {pole}')

    stav = vyhodnot(pole)
    if stav != '-':
      break
  
  if stav == 'x':
    print('Vyhrál/a jste! Gratuluji!')
  elif stav == 'o':
    print('Počítač vyhrál.')
  else:
    print('Remíza')

piskvorky1d()

