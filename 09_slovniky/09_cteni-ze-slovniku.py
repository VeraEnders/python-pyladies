#Ukol
# - Zeptej se uzivatele na jmeno, ktere chce vyhledat. Vrat mu prislusne telefonni cislo
# Bonus: Pokud zadane jmeno v seznamu neni, informuj uzivatele a ptej se znovu

zlate_stranky = {
    'Alice': '603888921',
    'Bohous': '777891776',
    'Cyril': '602345666',
    'Daniela': '728910000',
    'Eva': '777633798',
    'Filip': '608915433',
}

odpoved = input('Zadejte jmeno: ')

def vypis_tel_cislo(jmeno_hledane):
    for jmeno in zlate_stranky.keys():
        if jmeno == jmeno_hledane:
            return zlate_stranky[jmeno]

while True:
    tel_cislo = vypis_tel_cislo(odpoved)
    if tel_cislo:
        print(tel_cislo)
        break
    else:
        print('Vypada, ze zadane jmeno v seznamu neni, zkuste jine jmeno.')
        odpoved = input('Zadejte jmeno: ')
        
