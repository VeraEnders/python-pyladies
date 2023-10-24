# Nacitat ze souboru cisla, na kazdem radku jedno, a vratit nejmensi

nejmensi = None

def vrat_mensi(cislo):    
    global nejmensi
    if nejmensi is None or cislo < nejmensi:
        nejmensi = cislo

def nejmensi_cislo_ze_souboru(soubor):
    with open(soubor, encoding='utf-8') as soubor:
        for radek in soubor:
            cislo = int(radek)
            vrat_mensi(cislo)
    
nejmensi_cislo_ze_souboru('cisla.txt')
print(f'Nejmensi zadane cislo bylo {nejmensi}')