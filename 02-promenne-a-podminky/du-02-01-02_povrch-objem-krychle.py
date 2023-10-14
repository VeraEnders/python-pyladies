# Úkol 1
# Napiš program, který spočítá povrch a objem krychle o straně 2852 cm.
# Abys nemusela tolik hledat v učebnici (vlastně Wikipedii): povrch S = 6a², objem V = a³
# Řešení, pro kontrolu: S = 48803424 cm², V = 23197894208 cm³

strana_krychle = 2852 # cm
povrch = 6 * strana_krychle**2 # S = 6a²
objem = strana_krychle**3 # V = a³
print('Povrch krychle se stranou', strana_krychle, 'cm je', povrch, 'cm2')
print('Objem krychle se stranou', strana_krychle, 'cm je', objem, 'cm3')

# Úkol 2
# Změň program tak, aby délku strany mohl zadat uživatel.

strana_krychle = float(input('Zadej stranu krychle v centimentrech: '))

povrch = 6 * strana_krychle**2
objem = strana_krychle**3
print('Povrch krychle se stranou', strana_krychle, 'cm je', povrch, 'cm2')
print('Objem krychle se stranou', strana_krychle, 'cm je', objem, 'cm3')