'''
Ukol 2
Pomocí cyklu for napiš program, který vypíše:
1 na druhou je 1
2 na druhou je 4
3 na druhou je 9
4 na druhou je 16
Jak pojmenuješ proměnnou cyklu? Slovně zdůvodni.
'''

for cislo in range(1, 5):
  druha_mocnina = cislo ** 2
  print(cislo, 'na druhou je', druha_mocnina)

# Proměnná "cislo" reprezentuje čísla od 1 do 4, která budeme umocňovat na druhou.