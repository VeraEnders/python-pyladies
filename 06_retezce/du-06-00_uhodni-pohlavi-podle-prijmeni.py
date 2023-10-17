'''
Ukol 0
Vytvoř funkci, která dostane jako argument příjmení a zkusí podle něj uhodnout pohlaví. 
Funkce bude vracet řetězec "žena" nebo "muž". Funkce bude součástí programu, 
který se na příjmení zeptá a následně vypíše odhad pohlaví uživatele.
'''
def uhdni_pohlavi(prijmeni):
    if prijmeni[-3:] == "ová":
        return "žena"
    else:
        return "muž"

prijmeni_uzivatele = input("Zadejte vase prijmeni")
