cisla = [1, 2, 3, 4]

cisla[1:-1] = [0, 0, 0, 0, 0, 0]
print(cisla) # [1, 0, 0, 0, 0, 0, 0, 4]

cisla[1:-1] = []
print(cisla) # [1, 4]

# metoda del 
# smaže jednotlivé prvky seznamů, podseznamy, … a dokonce i proměnné
cisla1 = [1, 2, 3, 4, 5]
del cisla1[-1]
print(cisla1) # [1, 2, 3, 4]
del cisla1[3:5]
print(cisla1) # [1, 2, 3]
del cisla1
# print(cisla1) # NameError: name 'cisla1' is not defined

# metoda pop
# odstraní a vrátí poslední prvek v seznamu 
seznam = [1, 2, 3, 'abc', 4, 5, 6, 12]
posledni = seznam.pop()
print(posledni)  # 12
print(seznam)    # [1, 2, 3, 'abc', 4, 5, 6]

# metoda remove
# najde v seznamu daný prvek a odstraní ho
seznam.remove('abc')
print(seznam)    # [1, 2, 3, 4, 5, 6]

# metoda clear
# vyprázdní celý seznam
seznam.clear()
print(seznam)    # []