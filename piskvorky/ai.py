# Modul AI - jenom funkce tah_pocitace()

import util

'''
Napiš funkci tah_pocitace, která dostane řetězec s herním polem, vybere pozici, na kterou hrát, a vrátí herní pole se zaznamenaným tahem počítače.
Použij jednoduchou náhodnou „strategii”:
 - Vyber číslo od 0 do 19.
 - Pokud je dané políčko volné, hrej na něj.
 - Pokud ne, opakuj od bodu 1.
Můžeš předpokládat, že řetězec s herním polem vždy obsahuje alespoň jednu volnou pozici.
'''
# import random 

# def tah_pocitace(pole, symbol):
#   while True:
#     tah_nahodny = random.randrange(len(pole))

#     if pole[tah_nahodny] == '-':
#       pole_nove = util.tah(pole, tah_nahodny, symbol)
#       return pole_nove
    
# print(tah_pocitace('-' * 19, 'x'))
# print(tah_pocitace('-' * 19, 'o'))

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
      pole_nove = util.tah(pole, index + i, 'o')
      return pole_nove
    
  # Počítač se snaží umístit 'o' vedle symbolů 'x' protihráče
  array_x = ['-xx', 'x-x', 'xx-']

  for i in range(len(array_x)):
    index = pole.find(array_x[i])
    if index != -1:
      pole_nove = util.tah(pole, index + i, 'o')
      return pole_nove

  # Náhodné umístění 'o'
  while True:
    tah_nahodny = random.randrange(len(pole))

    if pole[tah_nahodny] == '-':
      pole_nove = util.tah(pole, tah_nahodny, 'o')
      return pole_nove