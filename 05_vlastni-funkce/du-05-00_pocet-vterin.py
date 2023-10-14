'''
Ukol 0
Vytvoř funkci pocet_vterin, která bude mít dva argumenty: čas v minutách a čas ve vteřinách. 
A bude vracet celkový počet vteřin.
'''

def pocet_vterin(minuty, vteriny):
  return minuty * 60 + vteriny

print(pocet_vterin(1, 60))