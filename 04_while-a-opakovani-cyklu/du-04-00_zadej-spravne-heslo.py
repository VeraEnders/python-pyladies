'''
Ukol 0
Napiš program, který se bude uživatele ptát na tajné heslo do té doby, než ho uživatel správně vyplní.
'''

tajne_heslo = 'ahoj'

while True:
  zadane_heslo = input('Zadej heslo: ')
  if zadane_heslo == tajne_heslo:
    print('Vítej!')
    break
  else:
    print('Špatně, zkus to znovu')