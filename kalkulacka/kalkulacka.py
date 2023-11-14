# Vytvorit soubor kalkulacka.py
# ktery bude vyuzivat modul operace, ve kterem bude deleni, nasobeni

# v kalkulacce se zeptejte na 2 cisla
# a operaci a tu provedte - ve smycce dokud ji neukonci

# bonus: vytvorte dalsi modul, ktery bude pocitat obsah a obvod obdelnika

import operace, obdelnik

def zadej_cisla():
    while True:
        try:
            a = int(input('Zadej cele cislo a: '))
            b = int(input('Zadej cele cislo b: '))
        except ValueError:
            print('MUsis zadat cislo! ')
        else:
            break
    return a, b

print('Vitej v kalkulacce! Zadej operaci, cokoliv jineho ukonci program. ')

while True:
    op = input('deleni nebo nasobeni? ')

    if op == 'deleni':
        a, b = zadej_cisla()
        try:
            print(operace.deleni(a, b))
        except ZeroDivisionError:
            print('Nelze delit nulou.')
    elif op == 'nasobeni':
        a, b = zadej_cisla()
        print(operace.nasobeni(a, b))
    else:
        break

print(f'Obsah obdelniku se stranami 5 a 4 je {obdelnik.obsah(5, 4)}')
print(f'Obvod obdelniku se stranami 5 a 4 je {obdelnik.obvod(5, 4)}')
