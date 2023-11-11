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

def vypis_tel_cislo(jmeno_hledane):
    # for jmeno in zlate_stranky.keys():
    #     if jmeno == jmeno_hledane:
    #         return zlate_stranky[jmeno]
    return zlate_stranky.get(jmeno_hledane)

while True:
    odpoved = input('Zadejte jméno: ')
    tel_cislo = vypis_tel_cislo(odpoved)
    if tel_cislo:
        print(tel_cislo)
        break
    else:
        print('Vypadá to, že zadané jméno v seznamu není, zkuste jiné jméno.')
        
