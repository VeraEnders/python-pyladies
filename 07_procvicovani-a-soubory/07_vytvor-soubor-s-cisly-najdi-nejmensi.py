# import random

# nejmensi = None

# def vrat_mensi(cislo):    
#     global nejmensi
#     if nejmensi is None or cislo < nejmensi:
#         nejmensi = cislo

# def nejmensi_cislo_ze_souboru(pocet_cisel, nazev):
#     with open(nazev, mode='w', encoding='utf-8') as soubor:
#         for cislo in range(pocet_cisel):
#             cislo = random.randrange(-100, 100)
#             print(cislo, file=soubor)
    
# nejmensi_cislo_ze_souboru(100, 'lot-of-numbers.txt')
# print(f'Nejmensi zadane cislo bylo {nejmensi}')