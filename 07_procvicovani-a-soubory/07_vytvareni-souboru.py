import random

# Vytvor funkci, ktera vygeneruje x cisel v rozsahu -100 do 100 do souboru,
# x a nazev souboru se zada jako argument
def vygeneruj_cisla_do_souboru(pocet_cisel, nazev):
    with open(nazev, mode='w', encoding='utf-8') as soubor:
        for cislo in range(pocet_cisel):
            cislo = random.randrange(-100, 100)
            print(cislo, file=soubor)

vygeneruj_cisla_do_souboru(100, 'novy_soubor.txt')

with open('druha_basnicka.txt', mode='w', encoding='utf-8') as soubor:
    print('Naše staré hodiny', file=soubor)
    print('Bijí', 2+2, 'hodiny', file=soubor)