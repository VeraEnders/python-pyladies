from math import sqrt, floor, ceil

cislo = int(input('Zadejte celé číslo: '))

druha_odmocnina = sqrt(cislo)
print('Druhá odmocnina z', cislo, 'je', druha_odmocnina)

cislo_zaokrouhlene_dolu = floor(druha_odmocnina)
cislo_zaokrouhlene_nahoru = ceil(druha_odmocnina)
print('Zaokrouhlené dolů:', cislo_zaokrouhlene_dolu, 'Zaokrouhlené nahoru', cislo_zaokrouhlene_nahoru)

################################

from math import sin, cos, tan, degrees, radians
# převod ze stupňů na radiány
uhel = radians(45)
print('Uhel 45 stupňů je', uhel)

# převod z radiánů na stupně
print('Uhel 1 radián je', degrees(1))

# sinus, kosinus, tangens
# počítají pro úhly v radiánech
print('Sinus 45° je', sin(uhel), 'radianů.')
print('Kosinus 45° je', cos(uhel), 'radianů.')
print('Tangens 45° je', tan(uhel), 'radianů.')