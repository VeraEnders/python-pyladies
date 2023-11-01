# sečítání seznamů a násobení číslem
# sečítat jde jen seznam se seznamem
melodie = ['C', 'E', 'G'] * 2 + ['E', 'E', 'D', 'E', 'F', 'D'] * 2 + ['E', 'D', 'C']
print(melodie)

# funkce len
print(len(melodie)) # 21

# metoda count
# Počet prvku v seznamu
pocet_d = melodie.count('D')
print(pocet_d) # 5

# metoda index
# Číslo první shody
prvni_d = melodie.index('D')
print(prvni_d) # 8

print('D' in melodie) # True
