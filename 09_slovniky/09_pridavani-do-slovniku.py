#Ukol
# - Zeptej se uzivatele na jmeno ktere chce pridat do seznamu
# - Pote se zeptej na telefonni cislo
# - Pridej ziskane polozky do telefoniho seznamu nize
# Bonus: Zkontroluj ze zadane cislo je cele cislo, jinak se ptej znovu
# Bonus: Zkontroluj zda dane jmenu v seznamu uz neni. Pokud tam je, ptej se znovu

zlate_stranky = {
    'Alice': '603888921',
    'Bohous': '777891776',
    'Cyril': '602345666',
    'Daniela': '728910000',
    'Eva': '777633798',
    'Filip': '608915433',
}

def pridej_do_slovniku(slovnik, jmeno, tel_cislo):
    slovnik[jmeno] = tel_cislo

def je_jmeno_ve_slovniku(slovnik, jmeno):
    return slovnik.get(jmeno)

while True:
    jmeno_zadane = input('Zadejte jméno: ')

    if not je_jmeno_ve_slovniku(zlate_stranky, jmeno_zadane):
        tel_cislo_zadane = input('Zadejte telefonní číslo: ')

        while len(tel_cislo_zadane) != 9:
            print('Telefonní číslo musi mít 9 číslic.')
            tel_cislo_zadane = input('Zadejte telefonní číslo: ')

        pridej_do_slovniku(zlate_stranky, jmeno_zadane, tel_cislo_zadane)
        print(zlate_stranky)
        break
    else:
        print('Vypadá to, že zadané jméno v seznamu není, zkuste jiné jméno.')