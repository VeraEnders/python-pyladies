def deleni(a, b):
    vysledek = a / b
    return vysledek

def vypis():
    cislo_a = int(input('Zadej cele cislo a: '))
    cislo_b = int(input('Zadej cele cislo b: '))
    print(deleni(cislo_a, cislo_b))

vstup = { 'a': 10, 'c': 5 }

def vypis_se_slovnikem(slovnik):
    print(deleni(slovnik['a'], slovnik['b']))

while True:
    try:
        vypis()
        # vypis_se_slovnikem(vstup)
    except ValueError:
        print('Musis zadat cele cislo!')
    except ZeroDivisionError:
        print('b nesmi byt 0!')
    except KeyError:
        print('Ve slovniku chybi hodnota! Zadejte cisla rucne: ')
        vypis()
        break
    except Exception:
        print('Nastala chyba, ukoncuji program.')
        break
    else:
        break
    finally:
        print('Toto se vypise vzdycky.')

print('Program dobehl na konec.')