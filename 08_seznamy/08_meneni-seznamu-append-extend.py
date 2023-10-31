# metoda append 
# přidání prvku na konec
# nic nevrací (resp. vrací None), ale „na místě” (angl. in place) změní seznam, na kterém pracuje
prvocisla = [2, 3, 5, 7, 11, 13, 17]
prvocisla.append(19)
print(prvocisla)

# Stejnou hodnotu může mít více proměnných
a = [1, 2, 3]   # vytvoření seznamu
b = a           # tady se nový seznam nevytváří, seznam vytvořený v prvním řádku má teď dvě jména: "a" a "b", ale stále pracujeme jenom s jedním seznamem
print(b)
a.append(4)
print(b)

# metoda extend 
# přidání víc prvků (seznamy, jednotlivé znaky řetězců, řádky souborů, čísla z range())
dalsi_prvocisla = [23, 29, 31]
prvocisla.extend(dalsi_prvocisla)
print(prvocisla)

seznam = []
seznam.extend('abcdef')
seznam.extend(range(10))
print(seznam)