'''
Ukol 5
Napiš program, který postupně načte od uživatele dvě čísla a jednoznakový řetězec – buď '+', '-', '*' nebo '/'. Program provede na číslech příslušnou operaci.

Příklad použití programu:

První číslo: 123
Druhé číslo: 456
Operace: +
123 + 456 = 579
'''

prvni_cislo = float(input('První číslo: '))
druhe_cislo = float(input('Druhé číslo: '))
operace = input('Operace (+, -, *, /): ')

if operace == '+' or operace == '-' or operace == '*' or operace == '/':
  
  if operace == '+':
    vysledek = prvni_cislo + druhe_cislo
  elif operace == '-':
    vysledek = prvni_cislo - druhe_cislo
  elif operace == '*':
    vysledek = prvni_cislo * druhe_cislo
  else:
    vysledek = prvni_cislo / druhe_cislo

  print(prvni_cislo, operace, druhe_cislo, '=', vysledek)

else:
  print('Nerozumím.')

