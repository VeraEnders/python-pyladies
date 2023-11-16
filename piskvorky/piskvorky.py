import util
import ai
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
        pole_nove = util.tah(pole, tah_input_cislo, 'x')
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

    pole = ai.tah_pocitace(pole)
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
