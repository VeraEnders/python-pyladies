'''
Ukol 1
Napiš funkci, která dostane jako argument identifikační číslo (např. rodné číslo, číslo platební karty, číslo OP) a která vrátí řetězec, kde jsou všechna čísla mimo posledních čtyř nahrazena symbolem X.

např. pro 1234567 funkce vrátí XXX4567
'''

def nahrad_cisla(id_cislo):
  id_text = str(id_cislo)
  delka_id = len(id_text)

  if delka_id <= 4:
    return 'Identifikační číslo musí obsahovat minimálně 5 znaků'
  
  retezec_x = 'X' * (delka_id - 4) 
  upraveny_retezec = retezec_x + id_text[-4:]

  return upraveny_retezec

print(nahrad_cisla(1234567))
print(nahrad_cisla(123))
