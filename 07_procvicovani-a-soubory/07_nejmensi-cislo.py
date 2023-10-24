# Program ktery se zepta na 5 cisel a vypise nejmensi

nejmensi = None

# funkce ktera dostane cislo a kdyz bude mensi nez to ulozene v "nejmensi" tak ho prepise

def vrat_mensi(cislo):
    global nejmensi
    
    if nejmensi is None or cislo < nejmensi:
        nejmensi = cislo

# funkce ktera se bude ptat uzivatele na cisla, tolikrat kolik zadame v parametru, a bude volat predchozi funkci
def zadej_cislo(pocet):
    for n in range(pocet):
        while True:
            cislo = input('Zadejte cislo: ')
            if not cislo.isdigit():
                print('Spatny vstup. Nezadal/a jste cislo.')
            else:
                vrat_mensi(int(cislo))
                break
    
# vypsani nejmensiho zjisteneho cisla
zadej_cislo(2)
print(f'Nejmensi zadane cislo bylo {nejmensi}')