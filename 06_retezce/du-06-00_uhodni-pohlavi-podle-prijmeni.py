'''
Ukol 0
Vytvoř funkci, která dostane jako argument příjmení a zkusí podle něj uhodnout pohlaví. 
Funkce bude vracet řetězec 'žena' nebo 'muž'. Funkce bude součástí programu, 
který se na příjmení zeptá a následně vypíše odhad pohlaví uživatele.
'''
def uhodni_pohlavi(prijmeni):
  for znak in prijmeni:
    if znak in '0123456789':
      return 'mimozemšťan'
  
  if prijmeni[-1] == 'á':
    return 'žena'
  else:
    return 'muž'

prijmeni_uzivatele = input('Zadejte Vaše příjmení: ')
pohlavi_uzivatele = uhodni_pohlavi(prijmeni_uzivatele)

print(f'Jste pravděpodobně {pohlavi_uzivatele}')