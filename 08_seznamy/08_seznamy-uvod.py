cisla = [1, 1, 2, 3, 5, 8, 13]
print(cisla)
print(cisla[2:-3])

# pomocí cyklu for můžeme procházet seznam po jednotlivých prvcích
for cislo in cisla:
  print(cislo)

# Hodnoty v seznamu mohou být jakéhokoli typu
seznam = [1, 'abc', True, None, range(10), len]
print(seznam)

# Měnění prvků
cisla_seznam = [1, 0, 3, 4]
cisla_seznam[1] = 2
print(cisla_seznam) # [1, 2, 3, 4]

cisla_seznam[1:-1] = [6, 5]
print(cisla_seznam) # [1, 6, 5, 4]

