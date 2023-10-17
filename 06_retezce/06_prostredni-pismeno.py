slovo = 'knihovna'

# najdi index prostredniho pismene
def index_prostredniho_pismene(slovo):
    celkova_delka = len(slovo)
    return celkova_delka // 2

print(slovo, index_prostredniho_pismene(slovo))

# vytvorte funkci prostredni_pismeno
# ma jako parametr slovo
# vrati prostredni pismeno
# pouzit funkci index_prostredniho_pismene

def prostredni_pismeno(slovo):
    index = index_prostredniho_pismene(slovo)
    return slovo[index]

print(slovo, prostredni_pismeno(slovo))