# Tento program rozdává nejapné rady do života.

print('Odpovídej "ano" nebo "ne". ')
stastna = input('Jsi šťastná? ')
if stastna == 'ano' or stastna == 'Ano':
  stastna = True
elif stastna == 'ne' or stastna == 'Ne':
  stastna = False
else:
  stastna = 0
  print('Nerozumím!')

bohata = input('Jsi bohatá? ')
if bohata == 'ano' or bohata == 'Ano':
  bohata = True
elif bohata == 'ne' or bohata == 'Ne':
  bohata = False
else:
  bohata = 0
  print('Nerozumím!')

if stastna == 0 or bohata == 0:
  print('Měla jsi odpovědět "ano" nebo "ne". Na shledanou')
elif stastna and bohata:
  print('Gratuluji!')
elif stastna:
  print('Zkus míň utrácet.')
elif bohata:
  print('Zkus se víc usmívat!')
else:
  print('To je mi líto.')