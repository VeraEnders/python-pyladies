# soubor = open('basnicka.txt', encoding='utf-8')
# obsah = soubor.read()
# soubor.close()

# print(obsah)


# příkaz `with` soubory zavírá automaticky
with open('basnicka.txt', encoding='utf-8') as soubor:
    # obsah = soubor.read()
    for radek in soubor:
        print(radek.rstrip())

# print(obsah)
